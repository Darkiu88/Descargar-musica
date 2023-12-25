# SoundFlexHub - Aplicación de Descarga de Videos a MP4

## Descripción

SoundFlexHub es una aplicación web construida con Flask y Pytube que permite a los usuarios descargar videos de YouTube en formato MP4. La aplicación también utiliza la biblioteca Pytube para obtener detalles del video, como el título, y permite al usuario seleccionar la carpeta de destino para la descarga.

## Requisitos

- **Python:** La aplicación está escrita en Python. Asegúrate de tener Python instalado en tu entorno de desarrollo.

## Configuración del Proyecto

1. **Instalar Dependencias:**
   ```bash
   pip install Flask pytube
Ejecutar la Aplicación:
bash
Copy code
python app.py
La aplicación estará disponible en http://localhost:5000.
Estructura del Código
app.py
El archivo principal que contiene la aplicación Flask.

python
Copy code
from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

def obtener_nombre_video(url):
    try:
        video = YouTube(url)
        return video.title
    except Exception as e:
        print(f"Error al obtener el título: {str(e)}")
        return "video_desconocido"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form['url']
    carpeta_destino = request.form['carpeta_destino']
    ruta_detino = os.path.join("/ruta/del/destino", carpeta_destino)

    try:
        nombre_video = obtener_nombre_video(url)
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        ruta_completa = os.path.join(ruta_detino, f"{nombre_video}.mp4")
        stream.download(ruta_completa)
        mensaje = f"Descarga completa: {nombre_video}"
    except Exception as e:
        mensaje = f"Error: {str(e)}"

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
Uso
Ejecuta app.py para iniciar la aplicación Flask.
Accede a http://localhost:5000 en tu navegador.
Ingresa la URL del video de YouTube y selecciona la carpeta de destino.
Haz clic en el botón de descarga.
La aplicación descargará el video en la carpeta especificada.

Contribuciones
¡Agradecemos las contribuciones! Si deseas contribuir, sigue los pasos estándar para solicitar pull requests en GitHub.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
## License

[MIT](https://choosealicense.com/licenses/mit/)

