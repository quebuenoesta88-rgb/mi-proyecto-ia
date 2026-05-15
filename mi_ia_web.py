import streamlit as st
from google import genai

# Ponemos la llave directamente aquí para que no haya pierde
llave = "AIzaSyB_hVxdR6sOOUCeR6XFQwcf4HIX0Pw1Idk"

client = genai.Client(api_key=llave)

st.set_page_config(page_title="IA de Emociones", page_icon="🌈")
st.title("🌈 Soy Prof. Jhonny Chipana Choque: aprendamos juntos")
st.write("¡Hola! Soy tu amigo IA. ¿Cómo te sientes hoy?")

usuario_input = st.text_input("Escribe aquí lo que quieras contarme:")

if st.button("Enviar a la IA"):
    if usuario_input:
        with st.spinner("Pensando..."):
            try:
                # Usamos el modelo directo
                response = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents=usuario_input
                )
                st.success("Un mensaje para ti:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
