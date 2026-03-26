import streamlit as st
import requests


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

st_slope = st.selectbox("ST Slope",["Up","Flat","Down"])


if st.button("Predict"):
  try:

      response = requests.post("http://127.0.0.1:8000/predict", json={
            "Age": age,
            "Sex": sex,
            "ChestPainType": chest_pain,
            "RestingBP": resting_bp,
            "Cholesterol": cholesterol,
            "FastingBS": fasting_bs,
            "RestingECG": resting_ecg,
            "MaxHR": max_hr,
            "ExerciseAngina": exercise_angina,
            "Oldpeak": oldpeak,
            "ST_Slope": st_slope
      })

      result = response.json()

      
      st.write(result['risk'])
  except Exception as e:
      st.error("Internal Server Error !")
      st.code(str(e))
