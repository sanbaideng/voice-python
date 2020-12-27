from moviepy.editor import *

video = VideoFileClip('muyu.mp4')
audio = video.audio.subclip(0,60)
audio.write_audiofile('muyu60.wav')