from flask import Flask, jsonify, request
from models.dog import post as create_dog, get as get_dog, put as update_dog, delete as delete_dog

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask!"

@app.route('/dogs', methods=['POST', 'GET', 'PUT', 'DELETE'])
def dogs():
    if str(request.method).upper() == 'POST':
        return jsonify(create_dog(request.json))
    if str(request.method).upper() == 'PUT':
        return jsonify(update_dog(request.json))
    if str(request.method).upper() == 'DELETE':
        return jsonify(delete_dog(request.json))
    dogs = get_dog()
    return jsonify(dogs)

@app.route('/dogs/<dog_id>')
def dog(dog_id):
    dog = get_dog({"id": dog_id})
    return jsonify(dog)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=6000)