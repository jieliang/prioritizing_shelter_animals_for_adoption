# api.py 
#1. generates web interface index.html
#2. gets user input from index.html
#3. uses model in api.py to make prediction based on user input
#4. sends prediction back to user at index.html


from flask import Flask, make_response, request, abort, jsonify, render_template
from api import make_soft_prediction

app = Flask(__name__)
app.debug = True

@app.route('/adoption_probability', methods=['POST'])
def get_sentiment_score():
    
    if not request.json or ('animalType' not in request.json) or ('intake_reproductive' not in request.json) or ('outcome_reproductive' not in request.json) or ('intake_health' not in request.json) or ('outcome_health' not in request.json):
        abort(400)

    animalType = request.json['animalType']
    intake_reproductive = request.json['intake_reproductive']
    outcome_reproductive = request.json['outcome_reproductive']
    intake_health= request.json['intake_health']
    outcome_health= request.json['outcome_health']
   
    score = make_soft_prediction(animalType,intake_reproductive,outcome_reproductive,intake_health,outcome_health)

    response = {
 
        'score': score
    }
    print('score =')
    print(score)
    return jsonify(response), 201

@app.route('/')
def index():
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run()

