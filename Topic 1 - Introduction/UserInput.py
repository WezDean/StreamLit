import streamlit as st 
import matplotlib.pyplot as plt 

st.title('Name and Age')
st.subheader('Enter the Information below')

with st.form("Who are you?"):
        Name = st.text_input('Enter Name:')
        Year = st.number_input('Enter Year of Bday:', min_value= 1940, max_value=2024)
        Age = 2024 - Year
        my_submit_button = st.form_submit_button()

if my_submit_button:
    st.write('Hello', Name, 'your age is', Age)