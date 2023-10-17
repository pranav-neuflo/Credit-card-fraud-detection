from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from fastapi.responses import JSONResponse
#from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
from typing import List

app = FastAPI()

# Load the Model
model = joblib.load("rf_credircard2.joblib")

# If possible, load the Scaler and Encoder used during training
scaler = joblib.load("scaler2.joblib")
encoder = joblib.load("encoder2.joblib")

class Item(BaseModel): 
    trans_date_trans_time: str
    cc_num: int
    merchant: str
    category: str
    amt: float
    first: str
    last: str
    gender: str
    street: str
    city: str
    state: str
    zip: int
    lat: float
    long: float
    city_pop: int
    job: str
    dob: str
    trans_num: str
    unix_time: int
    merch_lat: float
    merch_long: float

@app.post("/predict")
async def predict(item: Item):
    try:
        input_data = item.dict()
        print(item.dict())
        df = pd.DataFrame([input_data])
        processed_df = preprocess_data(df)
        predictions = model.predict(processed_df)
        df['is_fraud'] = predictions
        with open('prediction.csv', mode='a') as f:
            df.to_csv(f, header=f.tell() == 0, index=False)
        return {"prediction": predictions.tolist()}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    categorical_cols = ['merchant', 'category', 'gender', 'job']
    for col in categorical_cols:
        df[col] = encoder[col].transform(df[col])
    df_scaled = scaler.transform(df)
    return pd.DataFrame(df_scaled, columns=df.columns)
