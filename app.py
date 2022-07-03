from flask import Flask, jsonify, request
from scrapper import movies
app = Flask(__name__)

@app.route('/onpremiere', methods=['GET'])
def ping():
    response = jsonify(movies)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)

