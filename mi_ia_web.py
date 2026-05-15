import streamlit as st
from google import genai

# --- CONFIGURACIÓN ---
GEMINI_KEY = "AIzaSyD-4k8hI71raLjXBDieUNxTjkrxhFp85qU"
client = genai.Client(api_key=GEMINI_KEY)

# --- DISEÑO DE LA PÁGINA ---
st.set_page_config(page_title="IA de Emociones", page_icon="🌈")
st.title("🌈 Soy Prof. Jhonny Chipana Choque: aprendamos juntos")
st.write("¡Hola! Soy tu amigo IA para hablar preguntame lo que quieras. ¿Cómo te sientes hoy?")

# Entrada de texto para el niño
usuario_input = st.text_input("Escribe aquí lo que quieras contarme:", placeholder="Ej: Estoy feliz porque...")

if st.button("Enviar a la IA"):
    if usuario_input:
        with st.spinner("Pensando un consejo para ti..."):
            instruccion = f"Responde de forma cálida, breve y empática para un estudiante sobre esto: {usuario_input}"
            response = client.models.generate_content(
                model="gemini-1.5-flash", 
                contents=instruccion
            )
            st.success("Un mensaje para ti:")
            st.write(response.text)
