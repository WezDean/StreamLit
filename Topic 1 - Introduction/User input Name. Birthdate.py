import streamlit as st 
import matplotlib.pyplot as plt 

with st.form("Who are you?"):
    Name = st.text_input('Enter Name:')
    Birthdate = st.date_input('Enter Bday:')

st.write('Hello', Name, 'your birthdat is on the', Birthdate)