import streamlit as st
from PIL import Image

st.title("BMI Calculator App")

weight = st.number_input("what is your weight")
height = st.number_input("what is your height")

def bmi_index(weight,height):
    bmi = round(weight / (height**2),2)
    if bmi >= 30:
        return f'Your Bmi score is {bmi} and you are at risk of being extremely obese'
    elif bmi >= 25:
        return f'Your Bmi score is {bmi} and you are at risk of being overweight'
    elif bmi >= 18.5:
        return f'Your Bmi score is {bmi} and you are very healthy'
    else:
        return f'Your Bmi score is {bmi} and you are at risk of being underweight'
        
        
if st.button("calculate Bmi"):
    st.write( bmi_index(weight,height))