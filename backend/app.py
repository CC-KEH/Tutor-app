from fastapi import FastAPI, File, UploadFile ,BackgroundTasks, Response
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
import uuid
from main import store, run
import pickle
import shutil
import json
import os 

app = FastAPI()

tasks = []
master_objects = []

class format(BaseModel):
    id : Optional[UUID] = None
    number: Optional[int] = 10
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
        master_objects.append(master)
        # Save master object to db
    except Exception as e:
        print("error while making master object", e)
    
@app.post("/store_in_vector_db/")
async def store_to_db(background_tasks: BackgroundTasks):
    """For storing the pdfs and the Master object to respective databases."""
    
    try:
        background_tasks.add_task(store_in_background)
        return JSONResponse(content={"status": "Started storage"}, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/make_mcq/", response_model=format)
def make_mcq(task: format):
    task.id = str(uuid.uuid4())
    with open("backend/src/tutor/templates/quiz_template.json", 'r') as file:
        json_data = json.load(file)
        response_template = json.dumps(json_data, indent=4) 
    task.response_template = response_template
    
    tasks.append(task)
    
    master = master_objects[-1]

    result = run(master=master, task=task)

    return JSONResponse(content={"result": result}, status_code=200) 


@app.get("/history/", response_model=List[format])
def show_history():
    return tasks



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)