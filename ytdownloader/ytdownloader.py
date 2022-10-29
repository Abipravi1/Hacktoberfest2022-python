# Installing pytube library first
pip install pytube    

from pytube import YouTube
from sys import argv

# replace this youtube url with your yt video url u want to download
link = argv[1]
yt = YouTube('https://www.youtube.com/watch?v=CNFm_DzHDaE') 

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# replace the location below with location u want to save.Remember to add full location not relative.
yd.download('/content/drive/MyDrive')