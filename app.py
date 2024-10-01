import streamlit as st
from textblob import TextBlob
from googletrans import Translator
import time

translator = Translator()

st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f5;  
    }
    .title {
        color: #4B0082;  
    }
    .subheader {
        color: #FF1493;  
    }
    .text-area {
        background-color: #FFC0CB;  
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .stButton>button {
        background-color: #4B0082;  
        color: white;  
        border: None;  
        border-radius: 5px;  
        padding: 10px 20px;  
        font-size: 16px;  
        transition: background-color 0.3s ease;  
    }
    .stButton>button:hover {
        background-color: #6A5ACD;  
    }
    .loader {
        display: none;
        font-size: 20px;
        color: #FF1493;
        animation: blink 1s infinite;
    }
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Uso de TextBlob', anchor='textblob')
st.markdown('<h2 class="title">Uso de TextBlob</h2>', unsafe_allow_html=True)

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.markdown('<h3 class="subheader">Polaridad y Subjetividad</h3>', unsafe_allow_html=True)
    st.markdown("""
    **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
    
    **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ', key='text1', height=150)
    if text1:
        blob = TextBlob(text1)
        st.write('**Polaridad:** ', round(blob.sentiment.polarity, 2))
        st.write('**Subjetividad:** ', round(blob.sentiment.subjectivity, 2))
        x = round(blob.sentiment.polarity, 2)

        if x >= 0.5:
            st.write('**Resultado:** Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write('**Resultado:** Es un sentimiento Negativo 😔')
        else:
            st.write('**Resultado:** Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4', height=150)
    if text2:
        blob2 = TextBlob(text2)
        corrected_text = blob2.correct()
        st.markdown(f'<div class="text-area">{corrected_text}</div>', unsafe_allow_html=True)

if st.button("Convertir a Voz"):
    st.markdown('<div class="loader">Convirtiendo...</div>', unsafe_allow_html=True)
    time.sleep(2)
    if text1:
        result = translator.translate(text1, dest='en')
        st.success(f'Traducción a Inglés: {result.text}')
    else:
        st.warning("Por favor, ingrese un texto para convertir a voz.")


