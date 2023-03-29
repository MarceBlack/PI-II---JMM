import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('DASHBOARD DE KPIs') #Titulo
st.subheader('Rendimiento, Volatilidad e Índice Sharpe de 4 empresas del índice SP500, Standard & Poors 500 Index.') #Subtitulo
st.markdown('***') #Texto (los asteriscos generan una linea que corta mi pagina)

# Leer los archivos CSV generados previamente
df_combined = pd.read_csv('combined.csv')
df_AOS = pd.read_csv('AOS.csv')
df_AFL = pd.read_csv('AFL.csv')
df_ABT = pd.read_csv('ABT.csv')
df_PTC = pd.read_csv('PTC.csv')

# Crear una función para mostrar los KPI's
def kpis(df):
    st.write(f"Rendimiento: {round(df['Rendimiento'].iloc[-1], 2)}")
    st.write(f"Volatilidad: {round(df['Volatilidad'].iloc[-1], 2)}")
    st.write(f"Índice Sharpe: {round(df['Rendimiento'].iloc[-1] / df['Volatilidad'].iloc[-1], 2)}")

if st.checkbox('Mostrar DF AOS'): #Creamos un condicional con un nombre, con checkbox como condicional.
    st.dataframe(df_AOS) #Esta condicion desplega un dataframe.
    
if st.checkbox('Mostrar DF AFL'): #Creamos un condicional con un nombre, con checkbox como condicional.
    st.dataframe(df_AFL) #Esta condicion desplega un dataframe.

if st.checkbox('Mostrar DF ABT'): #Creamos un condicional con un nombre, con checkbox como condicional.
    st.dataframe(df_ABT) #Esta condicion desplega un dataframe.
    
if st.checkbox('Mostrar DF PTC'): #Creamos un condicional con un nombre, con checkbox como condicional.
    st.dataframe(df_PTC) #Esta condicion desplega un dataframe.
    
if st.checkbox('Vista de datos (Head o Tail)'): #Condicional Checkbox-Head
    if st.button('Mostrar head'): #Se crea el condicional button "Mostrar head"
        st.write(df_AOS.head()) #Write nos devuelve el texto de df.head
    if st.button('Mostrar tail'): ##Se crea el condicional button "Mostrar tail"
        st.write(df_AOS.tail()) #Write nos devuelve el texto de df.tail

if st.checkbox('Vista de datos (Head o Tail)'): #Condicional Checkbox-Head
    if st.button('Mostrar head'): #Se crea el condicional button "Mostrar head"
        st.write(df_AFL.head()) #Write nos devuelve el texto de df.head
    if st.button('Mostrar tail'): ##Se crea el condicional button "Mostrar tail"
        st.write(df_AFL.tail()) #Write nos devuelve el texto de df.tail

if st.checkbox('Vista de datos (Head o Tail)'): #Condicional Checkbox-Head
    if st.button('Mostrar head'): #Se crea el condicional button "Mostrar head"
        st.write(df_ABT.head()) #Write nos devuelve el texto de df.head
    if st.button('Mostrar tail'): ##Se crea el condicional button "Mostrar tail"
        st.write(df_ABT.tail()) #Write nos devuelve el texto de df.tail

if st.checkbox('Vista de datos (Head o Tail)'): #Condicional Checkbox-Head
    if st.button('Mostrar head'): #Se crea el condicional button "Mostrar head"
        st.write(df_combined.head()) #Write nos devuelve el texto de df.head
    if st.button('Mostrar tail'): ##Se crea el condicional button "Mostrar tail"
        st.write(df_combined.tail()) #Write nos devuelve el texto de df.tail
        
                
# Crear una página para cada empresa
st.set_page_config(page_title='Dashboard', page_icon=":bar_chart:", layout="wide")

# Página para AOS
st.write("# A.O. Smith Corporation (AOS)")
kpis(df_AOS)

# Página para AFL
st.write("# Aflac Incorporated (AFL)")
kpis(df_AFL)

# Página para ABT
st.write("# Abbott Laboratories (ABT)")
kpis(df_ABT)

# Página para PTC
st.write("# PTC Inc. (PTC)")
kpis(df_PTC)
