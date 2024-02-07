import streamlit as st 
import pandas as pd 

st.title('Titanic Analysis')
st.write('This Page shows various visualizations form the Titanic Dataset')
df = pd.read_csv('TitanicDataset.csv')
st.write(df.head())

df_dbh_grouped = pd.DataFrame(df.groupby(['age']).count()['survived'])
df_dbh_grouped.columns = ['fare']

st.write(df_dbh_grouped)

#create line chart
st.line_chart(df_dbh_grouped)

#line chart 2
st.line_chart(df['survived'])

#create bar chart
st.bar_chart(df_dbh_grouped)

#create area chart
st.area_chart(df_dbh_grouped)

#PLOTLY CHART
import plotly as px