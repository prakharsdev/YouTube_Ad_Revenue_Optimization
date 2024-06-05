import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load transformed data
df = pd.read_parquet('s3://youtube-data-bucket/processed/processed_data.parquet')

# Feature engineering
X = df[['views', 'likes']]
y = df['ad_revenue']  # Assuming ad_revenue is a column

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')
