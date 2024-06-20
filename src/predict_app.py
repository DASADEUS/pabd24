import os
from flask import Flask, render_template, request
from flask_cors import CORS
from joblib import load
import pandas as pd

MODEL_SAVE_PATH = 'models/my_model_regression_v01.joblib'

# Determine the absolute path to the directory containing templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'web'))

app = Flask(__name__, template_folder=template_dir)
CORS(app)

model = load(MODEL_SAVE_PATH)

def predict(total_meters: float) -> int:
    """ Predict house price from input data parameters.
    :param total_meters: house area in square meters.
    :raise Error: If something goes wrong.
    :return: House price, RUB.
    :rtype: int
    """
    price = model.predict(pd.DataFrame({'total_meters': [total_meters]}))
    return int(price.squeeze())

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict_web_serve():
    """Endpoint to predict house price."""
    if request.method == 'POST':
        total_meters = float(request.form['total_meters'])
        price = predict(total_meters)
        return render_template('index.html', prediction=f'Predicted price: {price:,} RUB')
    else:
        # Handle GET request, maybe render a form or redirect
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
