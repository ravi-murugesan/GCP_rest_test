from flask import Flask, request, redirect, url_for, flash, jsonify
# from sklearn import tree
# import numpy as np
# import pickle as p
import json


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def makecalc():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent' : some_joson})
    
    else:
        return jsonify({"about" : 'Hello World!'})


if __name__ == '__main__':
#     modelfile = 'final_prediction.pickle'
#     model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)

    
#     data = request.get_json()
#     prediction = np.array2string(model.predict(data))
#     return jsonify(prediction)
