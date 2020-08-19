from flask import Flask, request, redirect, url_for, flash, jsonify
import json


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def makecalc():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent' : some_json})
    
    else:
        return jsonify({"about" : 'Hello World!'})


if __name__ == '__main__':
    app.run(debug=True)
