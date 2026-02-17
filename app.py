import streamlit as st
import pandas as pd
import joblib

model = joblib.load('KNN_heart.pkl')
scaler = joblib.load('heart_scaler.pkl')
expected_columns = joblib.load('heart_columns.pkl')


st.title("Heart Disease Prediction By Siddharth")
st.markdown("Provide the following details to predict the likelihood of heart disease:")

age = st.slider("AGE",18,100,30)

sex = st.selectbox("SEX",['Male','Female'])

chest_pain = st.selectbox("Chest Pain Type",["ATA","NAP","TA","ASY"])

resting_bp = st.number_input("Resting Blood Pressure(mm Hg)",80,200,120)

cholesterol = st.number_input("Serum Cholesterol(mg/dl)",100,600,200) 

fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",[1,0]) 

resting_ecg = st.selectbox("Resting ECG",["Normal","ST","LVH"]) 

max_hr = st.slider("Max Heart Rate",60,220,150) 

exercise_angina = st.selectbox("Exercise Induced Angina",["YES","NO"]) 

oldpeak = st.slider("Oldpeak (ST Depression)",0.0,6.0,1.0) 

st_slope = st.selectbox("ST Slope",["Up","Flat","Down"])\


if st.button("Predict"):
  raw_input = {
    'Age': age,
    'RestingBP': resting_bp, 
    'Cholesterol': cholesterol, 
    'FastingBS': fasting_bs,
    'MaxHR': max_hr, 
    'Oldpeak': oldpeak,
    'Sex_'+ sex: 1, 
    'ChestPainType_'+ chest_pain: 1, 
    'RestingECG_'+ resting_ecg: 1, 
    'ExerciseAngina_'+ exercise_angina: 1, 
    'ST_Slope_'+ st_slope: 1 
  }


  input_df = pd.DataFrame([raw_input])
  
  for col in expected_columns:
    if col not in input_df.columns:
      input_df[col] = 0 

  input_df = input_df[expected_columns]

  scaled_input = scaler.transform(input_df)

  prediction = model.predict(scaled_input)[0]

  if prediction == 1:
    st.error("High Risk Of Heart Disease")
  else:
    st.success("Low Risk Of Heart Disease")