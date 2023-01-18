import streamlit as st
import pandas as pd
import numpy as np
from gsheetsdb import connect

df = st.cache(pd.read_csv, ttl=300)('df_x_SKBfregression_545noADME_withYandYpredandId.csv', sep=',', decimal='.')


# Create a connection object.
conn = connect()
sheet_url = "https://docs.google.com/spreadsheets/d/11QZjVGnbT3y7enxDc4IWCLcxy2gGpVQAfFoN8r3ytRM/edit#gid=0"
#sheet_url = st.secrets[public_gsheets_url]

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=1)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows


def onClick(a):
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    for row in rows:
        if( int(row.id)==int(a)):
            #st.write(int(row.id), row.feedback)
            texto = str(row.feedback)
            if (texto=="nan" or texto=="None"):
                texto=""
            st.text_area('Clique no botão abaixo para buscar dados da planilha de comentários', value=texto)   

  
id = st.selectbox( 'Selecione o identificador da modlécula', df['id'].unique()) 
'Você selecionou: ', id
st.write(df.iloc[[id], :])

#if st.checkbox('Show dataframe'):
#    st.write(diamonds)
st.button("Buscar comentário atualizado da planilha", on_click = onClick(id))

#texto = str(feedback.iloc[id, 1])
#'Texto: ', texto

#if (texto=="nan"):
#    texto=""

#txt = st.text_area('Feedback', value=texto)
#txt = st.text_input('Feedback', value=texto)


