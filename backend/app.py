from fastapi import FastAPI, File, UploadFile ,BackgroundTasks, Response
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from main import store, run
import pickle
import shutil
import json
import os 

app = FastAPI()

tasks = []

class format(BaseModel):
    id : Optional[UUID] = None
    number: Optional[UUID] = 10
    topics: str
    difficulty: Optional[str] = "easy"
    response_template: Optional[str] = ""
    question_type : str = "mcq"

UPLOAD_DIR = "backend/knowledge_store"

@app.get("/")
def read():
    return {"Hello": "World"}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...), memory: bool = False):
    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": file.filename}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/uploadmultiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...), memory: bool = False):
    file_urls = []
    try:
        for file in files:
            file_location = os.path.join(UPLOAD_DIR, file.filename)
            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            file_urls.append(file_location)
        return {"files": file_urls}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)



def store_in_background():
    try:
        flag, message, master = store(FOLDER_PATH=UPLOAD_DIR)
        # Save master object to db
        with open('backend/artifacts/master_objects/master_object.pkl', 'wb') as f:
            pickle.dump(master, f)
    except Exception as e:
        pass
    
@app.post("/store_in_vector_db/")
async def store_to_db(background_tasks: BackgroundTasks):
    """For storing the pdfs and the Master object to respective databases."""
    
    try:
        background_tasks.add_task(store_in_background)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/make_mcq/", response_model=format)
def make_mcq(task: format):
    task.id = uuid4()
    with open("backend/src/tutor/templates/quiz_template.json", 'r') as file:
        json_data = json.load(file)
        response_template = json.dumps(json_data, indent=4) 
    task.response_template = response_template
    
    tasks.append(task)
    
    with open("backend/artifacts/master_objects/master_object.pkl", 'rb') as f:
            # Deserialize the object from the file
            master = pickle.load(f)
    
    result = run(master=master,task=task)
    
    return {"result": result}   


@app.get("/history/", response_model=List[format])
def show_history():
    return tasks

# @app.get("/tasks/{task_id}", response_model=format)
# def read_task(task_id: UUID):
#     for task in tasks:
#         if task.id == task_id:
#             return task
        
#     raise HTTPException(status_code=404, detail="Task not found")

# @app.put("/tasks/{task_id}", response_model=Task)
# def update_task(task_id: UUID, task_update: Task):
#     for idx, task in enumerate(tasks):
#         if task.id == task_id:
#             updated_task = task.copy(update=task_update.dict(exclude_unset=True))
#             tasks[idx] = updated_task
#             return updated_task
        
#     raise HTTPException(status_code=404, detail="Task not found")

# @app.delete("/tasks/{task_id}", response_model=Task)
# def delete_task(task_id: UUID):
#     for idx, task in enumerate(tasks):
#         if task.id == task_id:
#             return tasks.pop(idx)
    
#     raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)