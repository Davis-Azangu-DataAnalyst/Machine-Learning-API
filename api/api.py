from fastapi import FastAPI,HTTPException, status, Query
import joblib
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class SepsisFeatures(BaseModel):
    PRG: float
    PL: float
    PR: float
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: int
    Insurance: object

@app.get("/")
def status_check():
    return {"status": "API is Online..."}

Logistic_Regression = joblib.load('./Toolkit/Logistic_Regression_pipeline.joblib')
SVC = joblib.load('./Toolkit/svc_pipeline.joblib')
encoder = joblib.load('./Toolkit/label_encoder.joblib')

@app.get('/', status_code=status.HTTP_200_OK)
def get_sepsis():
    return {'Title': 'Sepsis prediction API'}


@app.post('/predict_sepsis', status_code=status.HTTP_201_CREATED)
def predict_sepsis(data: SepsisFeatures, model: str = Query('Logistic_Regression', enum=['Logistic_Regression', 'SVC'])):
    df = pd.DataFrame([data.model_dump()])
 
    # Select the model based on the query parameter
    if model == 'Logistic_Regression':
        prediction = Logistic_Regression.predict(df)
        probability = Logistic_Regression.predict_proba(df)
    elif model == 'SVC':
        prediction = SVC.predict(df)
        probability = SVC.predict_proba(df)
   
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])[0]
    probability = probability[0]
 
    return {
        'model_used': model,
        'prediction': prediction,
        'probability': f'The probability of the prediction is {probability[0]:.2f}'
    }



