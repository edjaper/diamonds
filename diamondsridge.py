from sklearn.linear_model import Ridge
import streamlit as st
import pandas as pd
import sklearn_json as skljson

#!pip install lime
import lime
import lime.lime_tabular
import numpy as np


diamonds = st.cache(pd.read_csv)("diamonds.csv", sep=";", decimal=".")
feedback = pd.read_csv("feedback.csv", sep=";")


if "feedback" not in st.session_state:
    st.session_state['feedback'] = pd.DataFrame(columns=['id','feedback'])
    
#!pip install sklearn-json

#Loading up the Regression model we created
model = Ridge()
model = skljson.from_json('rr_model.json')


option = st.selectbox(
    'Which color do you like best?',
     diamonds['color'].unique())
'You selected: ', option

if st.checkbox('Show dataframe'):
    st.write(diamonds)
