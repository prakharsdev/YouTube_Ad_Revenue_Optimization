import pandas as pd
import joblib

# Load the model
model = joblib.load('model.pkl')

# Load new data for prediction
new_data = pd.DataFrame({
    'views': [5000],
    'likes': [500]
})

# Predict ad revenue
predictions = model.predict(new_data)
print(f"Predicted Ad Revenue: {predictions[0]}")
