#to run use:
#python -m streamlit run main.py 

import streamlit as st
import pandas as pd
import seaborn as sns
st.write("Hello World!")
st.title("This is a title")
st.number_input("Pick a number",0,10)
st.slider("Slide it",0,100,25)
st.text_area("Enter some text")
#STREAMLIT CHEATSHEET 


with st.sidebar:
    st.text_input("Filter by name")
    st.selectbox("Sort by",["A-Z","Z-A"])
    st.file_uploader("Upload a CSV")

#load data
@st.cache_data#to store data as cache memeory
#df=sns.load_dataset('iris')
#st.dataframe(df)
#image adding
#st.image("./ai-vs-human-vector.webp")