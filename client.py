import pandas as pd
import requests

# Define the endpoint
URL = "http://127.0.0.1:8000/predict"

# Load the dataset
data = pd.read_csv("test.csv")

# Function to send data to the API
def send_request(row):
    try:
        response = requests.post(URL, json=row)
        return response.json()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Send each row to the server
for index, row in data.iterrows():
    result = send_request(row.to_dict())
    print(f"Row {index} - Result: {result}")


