import streamlit as st
import pandas as pd
import numpy as np

df = st.cache(pd.read_csv)('df_x_SKBfregression_545noADME_withYandYpredandId.csv', sep=',', decimal='.')
feedback = st.cache(pd.read_csv, ttl=2)('feedback.csv', sep=';;#,;', decimal='.')

#if "feedback" not in st.session_state:
#    st.session_state['feedback'] = pd.DataFrame(columns=['id','feedback'])



def onSave(a, b):
    data = {
            'id':a,
            'feedback':b
        }
    st.session_state['feedback'] = st.session_state['feedback'].append(data, ignore_index=True)


    
    
id = st.selectbox( 'Which clarity do you like best?', df['id'].unique()) 
'You selected clarity: ', id
st.write(df.iloc[[id], :])

#if st.checkbox('Show dataframe'):
#    st.write(diamonds)

texto = str(feedback.loc[id, 'feedback'])
'Texto: ', texto

if (texto=="nan"):
    texto=""

txt = st.text_area('Feedback', value=texto)
txt = st.text_input('Feedback', value=texto)

st.button("Salvar", on_click = onSave(id, txt))
