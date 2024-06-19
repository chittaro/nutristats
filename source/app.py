from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


message = 'none'

# test getting dining halls
@app.route('/filter/halls', methods=['POST'])
def getHalls():
    request_data = request.get_json()
    print(request_data)
    message = request_data

@app.route('/', methods = ['GET'])
def home():
    return message


if __name__ == '__main__':
    app.run()