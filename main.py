import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


r = sr.Recognizer()

def record_audio(ask = False):
	with sr.Microphone() as source:
		if(ask):
			BURN_E_speak(ask)
		audio = r.listen(source)
		try:
			voice_data = r.recognize_google(audio)
		except sr.UnknownValueError:
			BURN_E_speak("I did not get that")
		except sr.RequestError:
			BURN_E_speak("sorry, I'm down")
		return voice_data

def BURN_E_speak(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r = random.randint(1, 1000000)
	audio_file = 'audio-' + str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)


def respond(voice_data):
	if "what is your name" in voice_data:
		BURN_E_speak("My name is BURN-E")
	if "what time is it" in voice_data:
		BURN_E_speak(ctime())
	if 'search' in voice_data:
		search =  record_audio('what do you want to search for?')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		BURN_E_speak("here is what i found for" + search)
	if 'find location' in voice_data:
		location =  record_audio('what is the location')
		url = 'https://google.com/maps/place/' + location + '/&amp;'
		webbrowser.get().open(url)
		BURN_E_speak("here is what i found for" + location)
	if 'exit' in voice_data:
		exit()

time.sleep(1)

BURN_E_speak("Hello how can I help")
while 1:
	voice_data = record_audio()
	respond(voice_data)
