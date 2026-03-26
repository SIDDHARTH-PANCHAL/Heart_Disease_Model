from fastapi import APIRouter
from app.schema import PatientData
from app.service import predict_heart

router  = APIRouter()

@router.get('/')
def home():
  return {'message':"Heart Disease Prediction API Running"}

@router.post('/predict')
def Predict_Data(data:PatientData):
  result = predict_heart(data)

  if result == 1:
    return{
      "prediction":1,
      "risk":"High Risk Of Heart Disease"
    }
  else:
    return{
      "prediction":0,
      "risk":"Low Risk Of Heart Disease"
    }


