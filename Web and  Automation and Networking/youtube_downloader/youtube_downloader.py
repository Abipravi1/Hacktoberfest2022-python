# Please install pytube using "pip install pytube" for this to work
from pytube import YouTube

url = input("YouTube link to download: ")

try:
    print("Checking YouTube link...")
    yt = YouTube(url)
    print("Video is available! Downloading...")
    # This downloads the highest resolution video stream
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("Done downloading video!")
except:
    print("Video at the provided link is unavailable!")
