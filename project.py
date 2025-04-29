import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

# Load dataset
df = pd.read_csv('Crop_recommendation.csv')

# Features and labels
features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
X = df[features]  #input
y = df['label']   #output

# Train-Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy check
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# Save model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved successfully!")