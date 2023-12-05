import streamlit as st
import pandas    as pd

col1, col2 = st.columns(2)
col1.write('Column 1')
col1.write('Column 2')

col1, col2, col3 = st.columns([3, 1, 1])

with col1 :
    st.image('https://i.imgur.com/n3eTzr2.jpg')

with col2 :
    st.image('https://i.imgur.com/n3eTzr2.jpg')

with col3 :
    st.image('https://i.imgur.com/n3eTzr2.jpg')

for i in range(10) :
    st.text(i)