from pydub import AudioSegment
sound = AudioSegment.from_file("muyu60.wav")
 
loudness = sound.dBFS
print(loudness)