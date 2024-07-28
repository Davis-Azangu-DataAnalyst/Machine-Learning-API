import streamlit as st
import pandas as pd
import requests

# Define backend url
backend_url = "http://api:80"

# function to set up page configuration
st.set_page_config(
        page_title="Sepsis Prediction",
        page_icon="🤖",
        layout="wide",
    )


def show_form():
    st.title("Sepsis Prediction App")
    with st.form('input-features'):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('🩺Blood Tests')
            PL = st.number_input('What is your blood work result 1?', min_value=0, max_value=200, value=0)
            SK = st.number_input('What is your blood work result 2?', min_value=0, max_value=200, value=0)
            TS = st.number_input('What is your blood work result 3?', min_value=0, max_value=1000, value=0)
            BD2 = st.number_input('What is your blood work results 4?', min_value=0, max_value=100, value=0)
        with col2:
            st.subheader('🏥Patients Vitals')
            PRG = st.number_input('What is your plasma glucose level?', min_value=0, max_value=100, value=0)
            PR = st.number_input('What is your pressure level?', min_value=0, max_value=200, value=0)
            M11 = st.number_input('What is your BMI ?', min_value=0, max_value=100, value=0)
            Age = st.number_input('What is your age?', min_value=0, max_value=150, value=0)
            Insurance = st.selectbox('Are you covered by insurance?', options=['1', '0'], key='Insurance')

        submit_button = st.form_submit_button('Predict status of sepsis')
        if submit_button:
         features = {'PRG': PRG, 'PL': PL, 'PR': PR, 'SK': SK, 'TS': TS, 'M11': M11, 'BD2': BD2, 'Age': Age, 'Insurance': Insurance}

         status_code = requests.get(backend_url).status_code
            
         if status_code == 200:
                response = requests.post(f"{backend_url}/predict_sepsis", json=features, timeout=60)
                 
                prediction = response.json()['prediction']
                st.success(f'The patient tested {prediction} for sepsis')
         else:
             st.error(f'Error: {response.json()["detail"]}')

if __name__ == '__main__':
    show_form() 
                
                
                
                
                
                
                
                
                       