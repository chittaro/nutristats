from flask import Flask, jsonify, request, session
from flask_cors import CORS
from analytics.filter import *

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


@app.route('/filter', methods = ['POST'])
def getFilters():
    if request.method == 'POST':
        response = request.json
        filtered = getBestItems(response['halls'], response['times'], response['sort'], response['ascending'])

        return {"message": "success", "data": filtered}


@app.route('/', methods = ['GET'])
def home():
    if not session.get('halls'):
        return 'no halls'
    else:
        return session.get('halls')


if __name__ == '__main__':
    app.run()