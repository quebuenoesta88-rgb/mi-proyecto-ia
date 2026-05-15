import os
import streamlit as st
import google.generativeai as genai



genai.configure(api_key=os.environ.get("GEMINI_API_KEY")

st.set_page_config(page_title="IA de Emociones", page_icon="🌈")
st.title("🌈 Soy Prof. Jhonny Chipana Choque: aprendamos juntos")
st.write("¡Hola! Soy tu amigo IA. ¿Cómo te sientes hoy?")

usuario_input = st.text_input("Escribe aquí lo que quieras contarme:")

if st.button("Enviar a la IA"):
    if usuario_input:
        with st.spinner("Pensando..."):
            try:
                # Usamos el modelo directo
               model = genai.GenerativeModel("gemini-2.0-flash")
               response = model.generate_content(usuario_input)
                st.success("Un mensaje para ti:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
