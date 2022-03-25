import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")
model = pickle.load(open("model_GYM.sav","rb"))

def predict_status(age, height, weight):
    input_data = np.asarray([[age, height, weight]])
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    st.title("Gym App")
    age = st.text_input("Enter your Age")
    height = st.text_input("Enter your Height in Feet")
    weight = st.text_input("Enter your Weight in Pounds")

    diagnosis = ''
    if st.button("Predict"):
        diagnosis = predict_status(age, height, weight)
        if diagnosis == "Underweight":
            st.info("You're Under Weight")
            st.markdown("Your Under weight, kindly add more proteins & carbs to become Healthy")

        elif diagnosis == "Healthy":
            st.success("You're Healthy")
            st.markdown("Your Healthy, kindly maintain the same diet")

        elif diagnosis == "Overweight":
            st.warning("You're Over Weight")
            st.markdown("Your Overweight, kindly reduce the carbs, add lean proteins & do the exercise")

        elif diagnosis == "Obese":
            st.error("Obesity!")
            st.markdown("Your Overweight, kindly reduce the carbs, add lean proteins & do the exercise")

        else:
            st.error("Extremely Obese")
            st.markdown("Your Overweight, kindly reduce the carbs, add lean proteins & do the exercise")

        st.subheader("what next? Take Action Towards Better Health")
        st.write("🙋🏼‍♂️ Maintaining a healthy weight is important for your heart health")
        st.write("🙋🏼‍♂️ Don't be like Spongebob or Patrik")
        st.write("Maintain a Healthy Weight: [ check right now!](https://www.nhlbi.nih.gov/heart-truth/maintain-a-healthy-weight)")

        st.write("## Thank you for Visiting \nProject by Gayathri")
        st.markdown("<h1 style='text-align: right; color: blue; font-size: small;'><a href='https://github.com/gayathrik948/Gym_app'>Looking for Source Code?</a></h1>",
                    unsafe_allow_html=True)
        # st.markdown("<h1 style='text-align: right; color: white; font-size: small'>you can find it on my GitHub</h1>", unsafe_allow_html=True)

if __name__=="__main__":
    main()


