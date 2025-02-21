# Proyecto de Cifrado con PyCryptodome y Cryptography

Este proyecto proporciona una interfaz gráfica sencilla utilizando **Streamlit** para cifrar y descifrar archivos de texto con dos métodos distintos de encriptación:
- **AES (Advanced Encryption Standard)** mediante la biblioteca **PyCryptodome**.
- **Fernet (Symmetric Encryption)** mediante la biblioteca **Cryptography**.

## 📂 Estructura del Proyecto

Una vez realizado el cifrado, la estructura de archivos se verá así:

```
Proyecto_cryptograpy/
│── README
├── proyecto_cryptodome/
│   ├── app.py
│   ├── archivos/
│   │   └── cifrado.txt  # Archivo cifrado generado
│ 
└── proyecto_cryptography/
    ├── app.py
    ├── archivos/
    │   └── cifrado.txt  # Archivo cifrado generado
```

## 🚀 Instalación y Uso

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/Proyecto_cryptography.git
cd proyecto_cryptography
```

### 2️⃣ Instalar Dependencias

Antes de ejecutar la aplicación, asegúrate de instalar las dependencias necesarias:
```bash
pip install streamlit pycryptodome cryptography
```

### 3️⃣ Ejecutar la Aplicación

Puedes ejecutar la aplicación en Streamlit con el siguiente comando:
```bash
streamlit run app.py
```
Dependiendo de qué versión desees probar, puedes hacerlo desde su respectiva carpeta:

**Para PyCryptodome:**
```bash
cd proyecto_cryptodome
streamlit run app.py
```

**Para Cryptography:**
```bash
cd proyecto_cryptography
streamlit run app.py
```

## 🛠️ Uso de la Aplicación
1. **Sube un archivo** de texto (`.txt`) a la aplicación.
2. Visualiza su contenido en la interfaz gráfica.
3. Presiona **"Cifrar"** para encriptar el contenido del archivo.
4. El archivo cifrado se almacenará en `archivos/cifrado.txt`.
5. Para recuperar el texto original, presiona **"Descifrar"**.

## 📌 Notas Importantes
- **PyCryptodome usa AES en modo EAX**, que requiere una clave de 16 bytes y un nonce para desencriptar correctamente.
- **Cryptography usa Fernet**, un sistema de cifrado simétrico basado en AES-128 con autenticación incorporada.
- Los archivos cifrados se guardan en la carpeta `archivos/`, asegúrate de no perder la clave generada al inicio de la sesión.

---

## 📄 Licencia
Este proyecto es de código abierto y se distribuye bajo la licencia MIT.