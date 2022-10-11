#!/usr/bin/env python3

from pytube import Playlist

def download_playlist():
	lista = Playlist(input("Insira a URL da playlist da qual deseja efetuar o download: "))
	print(f"Downloading: {lista.title}")
	for video in lista.videos:
		video.streams.filter(file_extension="mp4").first().download()
	print("Download concluído.")

download_playlist()

