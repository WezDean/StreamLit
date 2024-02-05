import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

st.title('Titanic')

selected_x_var = st.selectbox('Select X Variable:',
   ['sex', 'age', 'fare', 'class', 'survived'])

selected_y_var = st.selectbox('Select Y Variable:',
   ['sex', 'age', 'fare', 'class', 'survived'])

with st.form("Select File:"):
    Titanic = st.file_uploader('Select File')
    if Titanic is not None:    
        df = pd.read_csv(Titanic)
        my_submit_button = st.form_submit_button()
    else:
        my_submit_button = st.form_submit_button()
        st.stop()

gender = st.radio('Select Gender:', ['All', 'Male', 'Female'])

if my_submit_button:
    sns.set_style('darkgrid')

    if gender != 'All':
        # Filter the DataFrame based on the selected gender
        filtered_df = df[df['sex'] == gender.lower()]
    else:
        filtered_df = df

    if selected_x_var == 'sex':
        # Univariate histogram for the 'sex' variable
        sns.histplot(data=filtered_df, x=selected_x_var, hue='sex', multiple='stack')
        plt.xlabel(selected_x_var)
        plt.title(f'{selected_x_var} Histogram')
    else:
        # Bivariate histograms for other variables
        graph = sns.FacetGrid(filtered_df, col="sex", hue="sex")
        graph.map(sns.histplot, selected_x_var, alpha=0.7)
        graph.set_axis_labels(selected_x_var, "Count")

    st.pyplot(plt)
