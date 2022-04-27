import os
from moviepy.editor import *

#Get all mp4s:
files = os.listdir()
mp4s = []
for f in files:
    if ".mp4" in f:
        mp4s.append(f)
        print(f)

#convert
for mp4 in mp4s:


    audio = AudioFileClip(mp4)#video = VideoFileClip(mp4)    (this is for true mp4s)
    mp3Name = mp4[:-3]+"mp3"
    #print(mp3Name)
    audio.write_audiofile(mp3Name)#video.audio.write_audiofile(mp3Name)
