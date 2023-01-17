from sklearn.linear_model import Ridge
import streamlit as st
import pandas as pd
import sklearn_json as skljson
import lime
import lime.lime_tabular
import numpy as np


df = st.cache(pd.read_csv)('df_x_SKBfregression_545noADME_withYandYpredandId.csv', sep=',', decimal='.')

#if "feedback" not in st.session_state:
#    st.session_state['feedback'] = pd.DataFrame(columns=['id','feedback'])
    

id = st.selectbox( 'Which clarity do you like best?', df['id'].unique()) 
'You selected clarity: ', id
st.write(df[id])


#if st.checkbox('Show dataframe'):
#    st.write(diamonds)

    
    
