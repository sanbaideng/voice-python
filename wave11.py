from vad import VoiceActivityDetector

filename = 'muyu60.wav'
v = VoiceActivityDetector(filename)
v.plot_detected_speech_regions()