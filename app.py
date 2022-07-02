from flask import Flask, jsonify, request
from scrapper import movies
app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True, port=4000)

