# Importamos las bibliotecas necesarias
import streamlit as st  # Streamlit para crear la interfaz web
import os  # Módulo para manejar archivos en el sistema

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Título de la aplicación en la interfaz de Streamlit
st.title("Cifrado Pycryptodome - Codificación y Decodificación")

if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Inicializamos una variable para guardar el texto cifrado

# Generar clave y vector de inicialización (IV)
if "clave" not in st.session_state:
    st.session_state.clave = get_random_bytes(16)  # Inicializamos una variable para guardar la clave

if "nonce" not in st.session_state:
    st.session_state.nonce = None  # Inicializar nonce

if "tag" not in st.session_state:
    st.session_state.tag = None  # Inicializar el tag

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
        cipher = AES.new(st.session_state.clave, AES.MODE_EAX)
        caja = st.session_state.texto_cifrado.encode()
        cifrado, tag = cipher.encrypt_and_digest(caja)
        
        # Guardar el cifrador y el tag en el estado de la sesión
        st.session_state.cipher = cipher
        st.session_state.tag = tag
        
        # Mostramos información adicional sobre el texto a descifrar
        st.markdown(f"Aqui voy a cifrar:")
        st.markdown(f"Texto cifrado: `{cifrado}`")
        
        if not os.path.exists("archivos"):
            os.makedirs("archivos")
        
        # Guardamos el texto cifrado en un archivo
        with open("archivos/cifrado.txt", "wb") as f:
            f.write(cifrado)
        
        # Mostramos un mensaje de éxito
        st.success("Texto cifrado correctamente")
        
    # Botón para descifrar el texto
    if st.button("Descifrar"):
        # Solo descifrar
        st.markdown(f"Texto a descifrar:")
        if os.path.exists("archivos/cifrado.txt"):
            with open("archivos/cifrado.txt", "rb") as f:
                cifrado = f.read()
            
            cipher_dec = AES.new(st.session_state.clave, AES.MODE_EAX, st.session_state.cipher.nonce)
            mensaje_descifrado = cipher_dec.decrypt(cifrado).decode()
            st.markdown(f"Texto descifrado: `{mensaje_descifrado}`")