### Youtube Video Downloader
from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    """ Descarga el video en el path indicado """ 
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_streams = streams.get_highest_resolution()
        highest_res_streams.download(output_path=save_path)
        print(f"Video descargado correctamente.")

    except Exception as e:
        print(f"Ocurrio un error: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Carpeta seleccionada: {folder}")
    
    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Descarga Videos de Youtube")
    root.withdraw()

    video_url = input("Introduce una URL de un video de Youtube: ")
    save_dir = open_file_dialog()

    if save_dir:
        print(f"Comenzando descarga...espera")
        download_video(video_url, save_dir)
    else:
        print("Carpeta de destino inválida")