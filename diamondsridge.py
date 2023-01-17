import streamlit as st
import pandas as pd
import numpy as np

df = st.cache(pd.read_csv)('df_x_SKBfregression_545noADME_withYandYpredandId.csv', sep=',', decimal='.')
feedback = st.cache(pd.read_csv)('feedback.csv', sep=';;#,;', decimal='.')

#if "feedback" not in st.session_state:
#    st.session_state['feedback'] = pd.DataFrame(columns=['id','feedback'])
    
id = st.selectbox( 'Which clarity do you like best?', df['id'].unique()) 
'You selected clarity: ', id
st.write(df.iloc[[id], :])

#if st.checkbox('Show dataframe'):
#    st.write(diamonds)

if (not feedback.loc[id, 'feedback']):
    texto=""
else:
    texto = feedback.loc[id, 'feedback']

txt = st.text_area('Feedback', value=texto)

    
    
