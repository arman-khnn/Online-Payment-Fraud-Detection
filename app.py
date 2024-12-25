# fraud_detection_app/app.py

from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open(r"C:\Users\Arman Khan\OneDrive\Desktop\Project\onlinefraud.csv",'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def detect():
    try:
        data = request.get_json()
        # Format data as DataFrame according to model’s expected input structure
        features = pd.DataFrame([data])
        
        
        # Make prediction
        prediction = model.predict(features)
        result = 'Fraudulent' if prediction[0] == 1 else 'Legitimate'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
