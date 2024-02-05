import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

st.title("Palmer's Penguins")
st.markdown('Make Scatterplot')

selected_x_var = st.selectbox('Select X Variable:',
   ['bill_length_mm','bill_depth_mm', 'flipper_lenth_mm', 'body_mass_g'] )

selected_y_var = st.selectbox('Select Y Variable:',
   ['bill_length_mm','bill_depth_mm', 'flipper_lenth_mm', 'body_mass_g'] )


with st.form("Select File:"):
    penguin_file = st.file_uploader('Select Penguin File')
    if penguin_file is not None:    
        penguin_df = pd.read_csv(penguin_file)
        st.write(penguin_df)
        my_submit_button = st.form_submit_button()
    else:
        my_submit_button = st.form_submit_button()
        st.stop()


if my_submit_button:
    sns.set_style('darkgrid')
    markers = {'adelie': 'X', "Gentoo": 's', "Chinstrap": 'o'}

    fig, ax= plt.subplots()
    ax = sns.scatterplot(data=penguin_df, 
                        x = selected_x_var, y=selected_y_var, hue='species', markers=markers)

    plt.xlabel(selected_x_var)
    plt.ylabel(selected_y_var)
    plt.title('scatterplot penguin')
    st.pyplot(fig)
    