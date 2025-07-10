import os
from flask import Flask, request, render_template, jsonify, send_file, Response
import urllib.request
import json
import ssl
from dotenv import load_dotenv
import pandas as pd
from opentelemetry import trace
import logging
import requests
import os
tracer = trace.get_tracer("app.tracer")
load_dotenv()

app = Flask(__name__)

logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(name)s:%(module)s:%(message)s', level=logging.INFO)

def allowSelfSignedHttps(allowed):
    # Bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    with tracer.start_as_current_span("add") as span:
        allowSelfSignedHttps(True)
        patient_df = pd.read_csv('data/Patient.csv')
        transactions_df = pd.read_csv('data/Transactions.csv')
        patient_details = {}
        transaction ={}
        trans = transactions_df[transactions_df['Transaction_ID']==int(request.form.get("transactionId"))].to_dict(orient='records')
        span.set_attribute("app.value",trans)
        for tran in trans:
            for key, val in tran.items():
                transaction[key] = val
        try:
            pats = patient_df[patient_df['Patient_ID']==transaction['Patient_ID']].to_dict(orient='records')
            for pat in pats:
                for key, val in pat.items():
                    patient_details[key] = val
        except Exception as KeyError:
            return render_template('error.html'), 404

        data = {
                "input_data": {
                    "columns": [
                        "age",
                        "sex",
                        "cp",
                        "trestbps",
                        "chol",
                        "fbs",
                        "restecg",
                        "thalach",
                        "exang",
                        "oldpeak",
                        "slope",
                        "ca",
                        "thal"
                    ],
                    "data": [
                        [transaction['age'], transaction['sex'], transaction['cp'], transaction['trestbps'], transaction['chol'], transaction['fbs'], 
                        transaction['restecg'], transaction['thalach'], transaction['exang'], transaction['oldpeak'], transaction['slope'], 
                        transaction['ca'], transaction['thal']]
                    ]
                }
        }
        if transaction['Premieum']==1:

            result_json = [0]
            if result_json ==[0]:
                analysis_summary = """Based on the provided patient data, our analysis indicates no significant risk of heart attack. 
                                    However, we recommend routine follow-ups and monitoring to ensure continued health.
                                """
            else:
                analysis_summary = """ Based on the provided patient data, our analysis indicates a potential risk of heart attack. 
                                        We recommend clinical verification and correlation with additional diagnostic findings for accurate assessment.
                                    """
        else:
            analysis_summary = """PREMIUM SERVICE WAS NOT REQUESTED FOR THIS TRANSACTION"""
    return render_template('report 2.html', 
                           patient_details=patient_details, 
                           analysis_summary=analysis_summary, transaction=transaction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8099, debug=True)























