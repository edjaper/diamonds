import streamlit as st
import pandas as pd
import numpy as np

df = st.cache(pd.read_csv, ttl=300)('df_x_SKBfregression_545noADME_withYandYpredandId.csv', sep=',', decimal='.')
feedback = st.cache(pd.read_csv)('feedback.csv', sep=';;#,;', decimal='.')

#if "feedback" not in st.session_state:
#    st.session_state['feedback'] = pd.DataFrame(columns=['id','feedback'])



def onSave(a, b):
    df_feedback_save = feedback.copy()
    df_feedback_save.loc[a, 'feedback'] = b
    #st.session_state['feedback'] = st.session_state['feedback'].append(data, ignore_index=True)
    open('feedback.csv', 'w').write(df_feedback_save.to_csv())


    
id = st.selectbox( 'Which clarity do you like best?', df['id'].unique()) 
'You selected clarity: ', id
st.write(df.iloc[[id], :])

#if st.checkbox('Show dataframe'):
#    st.write(diamonds)

texto = str(feedback.iloc[id, 1])
'Texto: ', texto

if (texto=="nan"):
    texto=""

#txt = st.text_area('Feedback', value=texto)
txt = st.text_input('Feedback', value=texto)

st.button("Salvar", on_click = onSave(id, txt))
