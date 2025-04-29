from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array([[data['N'], data['P'], data['K'], data['temperature'], data['humidity'], data['ph'], data['rainfall']]])
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)