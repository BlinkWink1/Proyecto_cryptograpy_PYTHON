# Importamos las bibliotecas necesarias
import streamlit as st  # Streamlit para crear la interfaz web
import os  # Módulo para manejar archivos en el sistema
from cryptography.fernet import Fernet

# Título de la aplicación en la interfaz de Streamlit
st.title("Cifrado Fernet-Cryptography - Codificación y Decodificación")

if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Inicializamos una variable para guardar el texto cifrado

# Generar clave y cifrador
if "clave" not in st.session_state:
    st.session_state.clave = Fernet.generate_key()  # Generamos una clave secreta
    st.session_state.cipher = Fernet(st.session_state.clave)  # Creamos el cifrador

# Sección para subir un archivo de texto
archivo = st.file_uploader("Sube un archivo TXT", type=["txt"], key="file_uploader_1")

# Verificamos si el usuario ha subido un archivo
if archivo:
    texto = archivo.read().decode("utf-8")  # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    st.text_area("Contenido del archivo:", texto, height=200)  # Mostramos el contenido en un área de texto
    st.session_state.texto_cifrado = texto
    st.markdown(f"Aqui voy a cifrar:  `{st.session_state.texto_cifrado}`")

    # Botón para cifrar el texto
    if st.button("Cifrar"):
        # Cifrar
        mensaje = st.session_state.texto_cifrado.encode()
        mensaje_cifrado = st.session_state.cipher.encrypt(mensaje)
        
        # Guardar el mensaje cifrado en el estado de la sesión
        st.session_state.mensaje_cifrado = mensaje_cifrado
        
        # Mostramos información adicional sobre el texto a descifrar
        st.markdown(f"Aqui voy a cifrar:")
        st.markdown(f"Texto cifrado: `{mensaje_cifrado}`")
        
        if not os.path.exists("archivos"):
            os.makedirs("archivos")
        
        # Guardamos el texto cifrado en un archivo
        with open("archivos/cifrado.txt", "wb") as f:
            f.write(mensaje_cifrado)
        
        # Mostramos un mensaje de éxito
        st.success("Texto cifrado correctamente")
        
    # Botón para descifrar el texto
    if st.button("Descifrar"):
        # Solo descifrar
        st.markdown(f"Texto a descifrar:")
        if os.path.exists("archivos/cifrado.txt"):
            with open("archivos/cifrado.txt", "rb") as f:
                mensaje_cifrado = f.read()
            
            mensaje_descifrado = st.session_state.cipher.decrypt(mensaje_cifrado).decode()
            st.markdown(f"Texto descifrado: `{mensaje_descifrado}`")