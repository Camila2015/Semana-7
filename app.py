import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

# Estilo CSS para el fondo rosado en el texto
st.markdown(
    """
    <style>
    .text-area {
        background-color: pink;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Uso de textblob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
    
    Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ', key='text1', height=150)
    if text1:
        blob = TextBlob(text1)
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
        x = round(blob.sentiment.polarity, 2)
        
        if x >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
        else:
            st.write('Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4', height=150)
    if text2:
        blob2 = TextBlob(text2)
        corrected_text = blob2.correct()
        # Aplicar el fondo rosado al texto corregido
        st.markdown(f'<div class="text-area">{corrected_text}</div>', unsafe_allow_html=True)

