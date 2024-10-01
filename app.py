import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

# Estilo CSS para personalizar la apariencia de la app
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f5;  /* Color de fondo general */
    }
    .title {
        color: #4B0082;  /* Color del título */
    }
    .subheader {
        color: #FF1493;  /* Color del subtítulo */
    }
    .text-area {
        background-color: #FFC0CB;  /* Fondo rosado para el área de texto */
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .stButton>button {
        background-color: #4B0082;  /* Color de fondo de los botones */
        color: white;  /* Color del texto de los botones */
        border: None;  /* Sin borde */
        border-radius: 5px;  /* Esquinas redondeadas */
        padding: 10px 20px;  /* Espaciado dentro del botón */
        font-size: 16px;  /* Tamaño de fuente */
        transition: background-color 0.3s ease;  /* Transición suave para el color */
    }
    .stButton>button:hover {
        background-color: #6A5ACD;  /* Color al pasar el cursor */
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
        # Aplicar el fondo rosado al texto corregido
        st.markdown(f'<div class="text-area">{corrected_text}</div>', unsafe_allow_html=True)

# Botón para convertir texto a voz
if st.button("Convertir a Voz"):
    if text1:
        result = translator.translate(text1, dest='en')
        st.success(f'Traducción a Inglés: {result.text}')
    else:
        st.warning("Por favor, ingrese un texto para convertir a voz.")


