from backend.application import create_app
from flask import render_template, jsonify
import random
import requests
app = create_app()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index():
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.route('/api/getelec')
def get_elec_data():
    response = {
        'elec_data': [random.randint(1, 100) for i in range(12)]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()