from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

def obtener_nombre_video(url):
    try:
        video = YouTube(url)
        return video.title
    except Exception as e:
        print(f"Error al obtener el titulo: {str(e)}")
        return "video_desconosido"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/descargar', methods=['POST'])
def descargar():
    url= request.form['url']
    carpeta_destino = request.form['carpeta_destino']
    ruta_detino = os.path.join("/ruta/del/destino", carpeta_destino)


    try:
        nombre_video = obtener_nombre_video(url)
        video =  YouTube(url)
        stream = video.streams.get_highest_resolution()
        ruta_completa = os.path.join(ruta_detino, f"{nombre_video}.mp4")
        stream.download(ruta_completa)
        mensaje = f"Descarga completa: {nombre_video}"
    except Exception as e:
        mensaje = f"Error: {str(e)}"

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
