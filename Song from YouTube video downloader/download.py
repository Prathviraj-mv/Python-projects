import os
import pytube
# download oly audio(mp3) from Youtube.com
from pytube import YouTube

# set ur folder
path = "C:/yt"


def video_download():
    link = input("LINK:")
    video_link = YouTube(str(link))

    video = video_link.streams.last()
    video.download(path)


video_download()

# folder opens automatically
os.startfile("C:/yt")

