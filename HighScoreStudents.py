import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

st.title('Student Information')


df = pd.DataFrame({
    'Name': ['Zeus', 'Abby', 'Charlie', 'David'],
    'Age': [25,30,22,35],
    'Gender': ['Female', 'Male','Male','Male'],
    'Score': [85,92,78,88]
    })

# Get Student with the Highest Score
Top = df.loc[df['Score']==df['Score'].max()]
st.write('Student with the Highest Score:', Top)

# Students with the Age above 27
Older27 = df[df['Age'] > 27]
st.write('Students older than 27:', Older27)

AveScore = df['Score'].mean()
st.write('Average Class Score:', AveScore)

Big = df['Name'].sort_values()
st.write('Students with Big Dick Energy', Big)