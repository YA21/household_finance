from backend.application import create_app
from flask import render_template, jsonify, request
from flask_pymongo import PyMongo
import random

app = create_app()
app.config["MONGO_URI"] = "mongodb://localhost:27017/sampleDatabase"
mongo = PyMongo(app)

@app.route('/')
def index():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html", online_users=online_users)

@app.route('/api/getelec', methods=['GET'])
def get_elec_data():
    response = {
        'elec_data': [random.randint(1, 100) for i in range(12)]
    }
    for data in mongo.db.data.find():
        print(data)
    return jsonify(response)

@app.route('/api/update_elec', methods=['POST'])
def update_elec_data():
    mongo.db.data.insert({'month':request.json['month']})
    response = {
        "result": request.json['month']
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run()