from flask import Flask, request, jsonify
from connections import Gemini
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

@app.route('/api', methods=['GET', 'POST'])
def api():
    # model_response: {'message': 'Hello, World!'}
    if request.method == 'POST':
        model = Gemini()
        topics = request.json['topics'].split(',')
        difficulty = request.json['difficulty']
        question_count = request.json['question_count']
        model_response = model.generate_quiz(topics, difficulty, question_count)        
    
    return jsonify(model_response)

if __name__ == '__main__':
    app.run(debug=True)
