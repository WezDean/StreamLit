import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25,30,22,25],
    'Gender': ['Female', 'Male','Male','Male'],
    'Score': [85,92,78,88]
    })

st.write(data.Name)


