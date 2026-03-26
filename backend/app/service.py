import pandas as pd 
import joblib

model = joblib.load('model/KNN_heart.pkl')
scaler = joblib.load('model/heart_scaler.pkl')
expected_columns = joblib.load('model/heart_columns.pkl')

def predict_heart(data):
  raw_input = {
      'Age': data.Age,
      'RestingBP': data.RestingBP,
      'Cholesterol': data.Cholesterol,
      'FastingBS': data.FastingBS,
      'MaxHR': data.MaxHR,
      'Oldpeak': data.Oldpeak,
      'Sex_' + data.Sex: 1,
      'ChestPainType_' + data.ChestPainType: 1,
      'RestingECG_' + data.RestingECG: 1,
      'ExerciseAngina_' + data.ExerciseAngina: 1,
      'ST_Slope_' + data.ST_Slope: 1
  }

  input_df = pd.DataFrame([raw_input])

  # Fill missing columns
  for col in expected_columns:
    if col not in input_df.columns:
      input_df[col] = 0

  input_df = input_df[expected_columns]

  #scalar 
  scaled_input = scaler.transform(input_df)

  #prediction
  prediction = model.predict(scaled_input)[0]

  return int(prediction)
