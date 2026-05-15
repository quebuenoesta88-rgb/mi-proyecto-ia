import streamlit as st
from google import genai
import os

# Configuración de la llave
try:
    llave = st.secrets["GOOGLE_API_KEY"]
except:
    llave = "AIzaSyD-4k8hI71raLjXBDieUNxTjkrxhFp85qU"

client = genai.Client(api_key=llave)

st.set_page_config(page_title="IA de Emociones", page_icon="🌈")
st.title("🌈 Soy Prof. Jhonny Chipana Choque: aprendamos juntos")
st.write("¡Hola! Soy tu amigo IA para hablar. ¿Cómo te sientes hoy?")

usuario_input = st.text_input("Escribe aquí lo que quieras contarme:")

if st.button("Enviar a la IA"):
    if usuario_input:
        with st.spinner("Pensando..."):
            try:
                # MODELO CORREGIDO: gemini-1.5-flash (sin el models/ delante)
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=usuario_input
                )
                st.success("Un mensaje para ti:")
                st.write(response.text)
            except Exception as e:
                st.error("Error de conexión. Por favor, revisa la llave en Secrets.")
