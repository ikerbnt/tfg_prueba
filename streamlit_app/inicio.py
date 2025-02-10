import streamlit as st
from PIL import Image
import base64
import io

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()
# ------------------- CONFIGURACIÓN DE LA PÁGINA -------------------
def app():

    # Aplicar estilos

    # Cargar imagen
    # ESPAÑA = image_to_base64(Image.open("TFG/tfg/streamlit_app/templates/españa_icono.PNG"))
    # # ESPAÑA = image_to_base64(Image.open("streamlit_app/templates/españa_icono.PNG"))

    # # Título
    st.markdown("<div id=titulo>PREDICCIÓNSSSS DE TEMPERATURAS FUTURAS EN ESPAÑA</div>", unsafe_allow_html=True)

    # # Imagen principal
    # st.markdown(f"""
    #     <div id=imagen_centrada>
    #         <img src="data:image/png;base64,{ESPAÑA}">
    #     </div>
    # """, unsafe_allow_html=True)

