import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Central Limit Theorem')
st.subheader('Made my a black MF')

with st.form('first form:'):
    perc_heads = st.number_input(label='Chances of Head', min_value=.0,max_value=1.0)
    graph_title = st.text_input('Graph Title:')
    my_submit_button = st.form_submit_button()

binom_dist = np.random.binomial(1, perc_heads,1000)
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist,100, replace=True).mean())

fig, ax = plt.subplots()
ax = plt.hist(list_of_means, range=[0,1])
plt.title(graph_title)
st.pyplot(fig)