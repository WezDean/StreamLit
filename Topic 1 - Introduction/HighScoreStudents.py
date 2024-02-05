import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame({
    'Name': ['Zeus', 'Abby', 'Charlie', 'David'],
    'Age': [25,30,22,35],
    'Gender': ['Female', 'Male','Male','Male'],
    'Score': [85,92,78,88]
    })

st.title('Student Information')

# Create a new student with input validation
new_name = st.text_input('Enter new student name:')
new_gender = st.selectbox('Select gender:', ['Male', 'Female'])
new_age = st.number_input('Enter age (whole number up to 50):', min_value=0, max_value=50, step=1)
new_score = st.number_input('Enter score (between 0 and 100):', min_value=0, max_value=100, step=1)

# Add new student to the dataframe
if st.button('Add Student'):
    new_student = pd.DataFrame({
        'Name': [new_name],
        'Age': [new_age],
        'Gender': [new_gender],
        'Score': [new_score]
    })
    df = pd.concat([df, new_student], ignore_index=True)
    st.success(f'{new_name} has been added to the student list.')

# Get Student with the Highest Score
Top = df.loc[df['Score'] == df['Score'].max()]
st.write('Student with the Highest Score:', Top)

# Students with the Age above 27
Older27 = df[df['Age'] > 27]
st.write('Students older than 27:', Older27)

AveScore = df['Score'].mean()
st.write('Average Class Score:', AveScore)

# Display students sorted by name
Students = df.sort_values(by='Name')
st.write('Students sorted by name:', Students)
