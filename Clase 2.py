import datetime 
import time 
import pandas as pd
import streamlit as st
from PIL import Image  # "Image" en lugar de "image"

st.title("Titulo: Analitica de Datos")  # "title" en lugar de "tittle"
st.header("Este es un header")
st.subheader("Este es un subheader")

st.text("Texto: Hola Streamlit")
st.markdown("# Este es un markdown h1 \n ## Este es un h2 \n ### Este es un h3 ")  # Corregir "matkdown" a "markdown"
st.success("Succesful!")  # Corregir "succes" a "success"
st.info("Información")
st.warning("Warning")  # "Warning" con mayúscula
st.error("Error")
# st.exception("Name Error (No esta definido)")  # No hay función "exception" en Streamlit
st.header("Obtener informacion de ayuda de Python")
st.help(range)
st.header("Widget")


