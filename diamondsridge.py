import streamlit as st
import pandas as pd
import numpy as np

df = st.cache(pd.read_csv)('df_x_SKBfregression_545noADME_withYandYpredandId.csv', sep=',', decimal='.')

#if "feedback" not in st.session_state:
#    st.session_state['feedback'] = pd.DataFrame(columns=['id','feedback'])
    
id = st.selectbox( 'Which clarity do you like best?', df['id'].unique()) 
'You selected clarity: ', id
st.write(df.iloc[[id], :])

#if st.checkbox('Show dataframe'):
#    st.write(diamonds)

txt = st.text_area('Feedback', value="teste 1 \nteste 2 \n t t t\no")

    
    
