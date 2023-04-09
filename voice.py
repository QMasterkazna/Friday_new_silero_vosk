import pyttsx3		#pip install pyttsx3
import torch
import sounddevice as sd
import time

#Инициализация голосового "движка" при старте программы
#
#Голос берется из системы, первый попавшийся
#
#Доп материал:
#https://pypi.org/project/pyttsx3/
#https://pyttsx3.readthedocs.io/en/latest/
#https://github.com/nateshmbhat/pyttsx3
#На Linux-ax, скорее всего нужно еще:
#sudo apt update && sudo apt install espeak ffmpeg libespeak1
#
engine = pyttsx3.init()
engine.setProperty('rate', 180)				#скорость речи


def speaker(text):
	'''Озвучка текста'''
	engine.say(text)
	engine.runAndWait()

#
# def speaker(text):
# 	language = 'ru'
# 	model_id = 'ru_v3'
# 	sample_rate = 48000
# 	speaker = 'baya'
# 	put_accent = True
# 	device = torch.device('cpu')
# 	text = text
# 	model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
# 							  model='silero_tts',
# 							  language=language,
# 							  speaker=model_id)
# 	model.to(device)
# 	audio = model.apply_tts(text=text,
# 							speaker=speaker,
# 							sample_rate=sample_rate,
# 							put_accent=put_accent)
# 	print(text)
# 	sd.play(audio, samplerate=sample_rate)
# 	time.sleep(len(audio) / sample_rate)
# 	sd.stop()
