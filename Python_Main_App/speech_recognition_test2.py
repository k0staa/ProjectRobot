#!./py3env/bin/python

# NOTE: this example requires PyAudio because it uses the Microphone class

import time
import pprint

import speech_recognition as sr

WIT_AI_KEY = "GET FROM SECRET FILE"  # Wit.ai keys are 32-character uppercase alphanumeric strings


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    wit_answer = r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)
    print("Wit.ai thinks you said ")
    pprint.pprint(wit_answer)
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

