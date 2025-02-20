from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("xgboost_maintenance_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Expecting JSON input
    df = pd.DataFrame([data])  # Convert JSON to DataFrame
    
    prediction = model.predict(df)
    
    return jsonify({"predicted_maintenance_bill": float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
