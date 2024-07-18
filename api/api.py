from fastapi import FastAPI
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

Logistic_pipeline = joblib.load('../models/Logistic_Regression_Pipeline.joblib')
encoder = joblib.load('../models/label_encoder.joblib')

@app.post('/logistic_prediction')
def predict_sepsis(data:SepsisFeatures):

 # Convert the input data to a pandas DataFrame
    df = pd.DataFrame([data.model_dump()])

# Make a prediction using the loaded logistic regression model
    prediction = Logistic_pipeline.predict(df)

# Get the probabilities for the prediction
    probabilities = Logistic_pipeline.predict_proba(df)

# Get the probability of the predicted class
    probability = max(probabilities[0])


# Convert the prediction to an integer and map it to the original label
    prediction = int(prediction[0])

# Reverse the label encoding to get the original prediction label
    prediction = encoder.inverse_transform([prediction])[0]


    
    

    return {"prediction":prediction,
            "probability": probability}

    



svc_pipeline = joblib.load('../models/svc_pipeline.joblib')
encoder = joblib.load('../models/label_encoder.joblib')

@app.post('/svc_prediction')
def predict_svc(data: SepsisFeatures):

     # Convert the input data to a pandas DataFrame
    df = pd.DataFrame([data.model_dump()])
    
 # Make a prediction using the loaded SVC model
    prediction = svc_pipeline.predict(df)

    # Get the probabilities for the prediction
    probabilities = svc_pipeline.predict_proba(df)

    # Get the probability of the predicted class
    probability = max(probabilities[0])

    # Convert the prediction to an integer and map it to the original label
    prediction = int(prediction[0])

    # Reverse the label encoding to get the original prediction label
    prediction = encoder.inverse_transform([prediction])[0]

    return {"prediction": prediction, "probability": probability}


