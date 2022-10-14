from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""

    LOG.info("Scaling Payload: %s payload")
    scaler = StandardScaler(with_mean=False).fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")

def home():
    html = "<h3>Sklearn Prediction Home (test)</h3>"
    return html.format(format)

'''
def home():
    html = '<h1>Sklearn Prediction Home</h1>\
    <p>This is a serverless flask webapp</p>\
    <p>It uses machine learning to predict the prices of houses</p>\
    <p>Click this link for more information <a href="https://github.com/Rbaibi/CI-CD-Pipeline-for-house-prediction">link</a>.</p>\
    <img src="https://media.istockphoto.com/vectors/blue-house-outline-vector-id164724113?k=20&m=164724113&s=612x612&w=0&h=GJPOwUmovJ0R2i-3Qd2jcnq5Wmv2p_ZqxJdMHUGBYwA="/>'
    return html.format(format)
'''
# TO DO:  Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction

    input looks like:
            {
    "CHAS":{
      "0":0
    },
    "RM":{
      "0":6.575
    },
    "TAX":{
      "0":296.0
    },
    "PTRATIO":{
       "0":15.3
    },
    "B":{
       "0":396.9
    },
    "LSTAT":{
       "0":4.98
    }

    result looks like:
    { "prediction": [ 20.35373177134412 ] }

    """

    try:
        clfcon = joblib.load("boston_housing_prediction.joblib")
        clf = clfcon[0][0]
    except:
        LOG.info("JSON payload: %s json_payload")
        return "Model not loaded"

    json_payload = request.json
    LOG.info("JSON payload: %s json_payload")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("inference payload DataFrame: %s inference_payload")
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
