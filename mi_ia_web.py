import streamlit as st
from google import genai
import os

# Configuración de la llave desde los "Secrets" de Streamlit
try:
    GEMINI_KEY = st.secrets["GOOGLE_API_KEY"]
except:
    GEMINI_KEY = os.environ.get("GOOGLE_API_KEY")

client = genai.Client(api_key=GEMINI_KEY)

# DISEÑO DE LA PÁGINA
st.set_page_config(page_title="IA de Emociones", page_icon="🌈")
st.title("🌈 Soy Prof. Jhonny Chipana Choque: aprendamos juntos")
st.write("¡Hola! Soy tu amigo IA para hablar, pregúntame lo que quieras. ¿Cómo te sientes hoy?")

usuario_input = st.text_input("Escribe aquí lo que quieras contarme:", placeholder="Ej: Estoy feliz porque...")

if st.button("Enviar a la IA"):
    if usuario_input:
        with st.spinner("Pensando un mensaje para ti..."):
            try:
                instruccion = f"Responde de forma cálida, breve y empática para un estudiante sobre esto: {usuario_input}"
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=instruccion
                )
                st.success("Un mensaje para ti:")
                st.write(response.text)
            except Exception as e:
                st.error("Hubo un pequeño problema. Revisa si la clave API en 'Secrets' es correcta.")
    else:
        st.warning("Por favor, escribe algo primero.")
