import streamlit as st
from PIL import Image
import base64
import io

# ------------------- CONFIGURACIÓN DE LA PÁGINA (Debe ser lo primero) -------------------
# icon = Image.open("TFG/tfg/streamlit_app/templates/aemet_icono.png") 
# st.set_page_config(
#     page_title="TFG IBD",
#     page_icon=icon,  
#     layout="wide", 
#     initial_sidebar_state="collapsed"
# )

# ------------------- CONVERTIR IMAGEN A BASE64 -------------------
# def image_to_base64(image):
#     buffered = io.BytesIO()
#     image.save(buffered, format="PNG")
#     return base64.b64encode(buffered.getvalue()).decode()

# # Cargar y convertir las imágenes a base64
# ICONO = image_to_base64(Image.open("TFG/tfg/streamlit_app/templates/aemet_icono.png"))
# BANDA_NWORLD = image_to_base64(Image.open("TFG/tfg/streamlit_app/templates/banda_nworld.PNG"))
# BLACK = image_to_base64(Image.open("TFG/tfg/streamlit_app/templates/black.jpg"))
# ICONO = image_to_base64(Image.open("streamlit_app/templates/aemet_icono.png"))
# BANDA_NWORLD = image_to_base64(Image.open("streamlit_app/templates/banda_nworld.PNG"))
# BLACK = image_to_base64(Image.open("streamlit_app/templates/black.jpg"))



# ------------------- ESTILOS COMUNES -------------------
def estilos_comunes():
    # Configuración inicial de la página


    st.markdown(f"""<style>
        
        /********************************************************************/


        .stApp {{
            margin: auto;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            overflow: auto;
            background: linear-gradient(315deg, #4f2991 3%, #7dc4ff 38%, #36cfcc 68%, #a92ed3 98%);
            animation: gradient 15s ease infinite;
            background-size: 400% 400%;
            background-attachment: fixed;
        }}

        /* Header personalizado */
        header[data-testid="stHeader"] {{
            background-color: salmon;
            z-index: 1;
        }}
        
        /********************************************************************/

        /* Estructura general */

        
        /********************************************************************/

        #titulo {{
            font-size: 30px !important;
            font-weight: bold;
            color: red;
            text-align: center;
        }}
            
        #texto_centrado {{
            text-align: center;
        }}
        
        #imagen_centrada {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        
        /********************************************************************/

/* ESTILO PARA RADIO BUTTON CON FONDO TRANSPARENTE */
        .stRadio div {{
            font-size: 28px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-weight: bold;
            margin: 3px 0px;
            background-color: salmon; /* Fondo para el botón */
            font-family: 'Courier New', monospace;
            padding: 3px 7px; /* Espaciado interno */
            z-index: 2; 
        }}

        /* Escondemos el texto del label */
        div.stRadio > label {{
            display: none; /* Ocultar el texto del label */
        }}

        /* Estilo del hover aplicado al input de tipo radio */
        .stRadio input[type="radio"]:not(:checked) + div:hover {{
            background-color: orange; /* Color de fondo en hover */
            transition: background-color 0.3s ease; /* Transición suave */
            border-radius: 10px;
        }}

        /* Estilo para cuando el radio está seleccionado */
        .stRadio input[type="radio"]:checked + div {{
            background-color: grey; /* Color gris cuando está seleccionado */
            color: white;
            border-radius: 10px;
        }}

        /* Opcional: cambiar el cursor al pasar por encima del radio */
        .stRadio input[type="radio"]:not(:checked) + div:hover {{
            cursor: pointer;
        }}


       /********************************************************************/

        /* AJUSTE DEL CONTENEDOR PRINCIPAL */
        .block-container {{
            padding: 0px 0px !important; /* 20px arriba y abajo, 10px en los laterales */
            margin-top: 0px;        }}


        /********************************************************************/

        /* FOOTER */
        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            background-color: white;
            text-align: center;
            padding: 5px;
            box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            margin-top: auto;
            z-index: 9999; /* Asegura que el footer esté por encima del contenido */
            background: salmon;
        
        }}
        

        /********************************************************************/

    </style>""", unsafe_allow_html=True)

    # ------------------- FOOTER -------------------
    # st.markdown(f"""
    # <div class="footer">
    #     <div style="color: white;">© 2025 - TFG IBD | Datos obtenidos de AEMET</div>
    #     <div id="imagen_centrada">
    #         <img src="data:image/png;base64,{ICONO}" width="25">
    #     </div>
    # </div>
    # """, unsafe_allow_html=True)

# ------------------- CARGAR CONTENIDO SEGÚN LA OPCIÓN -------------------
def main():
    estilos_comunes()
    
    opcion = st.radio('', ['🏠 INICIO', '📂 ANÁLISIS', '📊 PREDICCIONES'], horizontal=True, index=0)
    
    if opcion == '🏠 INICIO':
        import inicio
        inicio.app()
    elif opcion == '📂 ANÁLISIS':
        import analisis
        analisis.app()
    elif opcion == '📊 PREDICCIONES':
        import predicciones
        predicciones.app()

if __name__ == "__main__":
    main()

