from application import create_app
from flask import jsonify, request
import random

APP = create_app()

@APP.route('/api/getelec', methods=['GET'])
def get_elec_data():
    response = {
        'elec_data': [random.randint(1, 100) for i in range(12)]
    }
    return jsonify(response)

@APP.route('/api/update_elec', methods=['POST'])
def update_elec_data():
    response = {
        "result": request.json['month']
    }
    return jsonify(response)

if __name__ == '__main__':
    APP.run(host="0.0.0.0", port=5000, debug=True)