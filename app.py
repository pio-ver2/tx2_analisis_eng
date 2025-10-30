import streamlit as st
from textblob import TextBlob
from googletrans import Translator


st.markdown("""
    <style>
        body {
            background-color: #e0f7fa;  
        }
    </style>
""", unsafe_allow_html=True)


translator = Translator()

st.title('💬 **Análisis de Sentimientos con TextBlob**')
st.subheader("Escribe una frase en el campo de texto para analizar su polaridad y subjetividad 😊")


with st.sidebar:
    st.subheader("📊 **Polaridad y Subjetividad**")
    st.write("""
        **Polaridad:** Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
        
        **Subjetividad:** Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo 
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)


with st.expander('🔍 **Analizar Polaridad y Subjetividad en un texto**'):
    text1 = st.text_area('Escribe el texto para analizar:', '')
    if text1:
  
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        
   
        blob = TextBlob(trans_text)
        
        st.write('📈 **Polaridad:**', round(blob.sentiment.polarity, 2))
        st.write('🔍 **Subjetividad:**', round(blob.sentiment.subjectivity, 2))
        

        x = round(blob.sentiment.polarity, 2)
        if x >= 0.5:
            st.write('✨ **Sentimiento Positivo!** 😊')
        elif x <= -0.5:
            st.write('💔 **Sentimiento Negativo!** 😔')
        else:
            st.write('😐 **Sentimiento Neutral**')


with st.expander('🔧 **Corrección del texto en inglés**'):
    text2 = st.text_area('Escribe el texto en inglés para corregir:', '', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write('🔄 **Texto corregido:**')
        st.write(blob2.correct())
