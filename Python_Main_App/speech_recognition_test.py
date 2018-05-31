#!./py3env/bin/python

# NOTE: this example requires PyAudio because it uses the Microphone class

import time
import pprint
import speech_recognition as sr
from utilities import RobotUtils

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Send to recognize!")
        WIT_AI_KEY = "GET FORM SECRET FILE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
        wit_answer = recognizer.recognize_wit(audio,key=WIT_AI_KEY, show_all=True)
        print("Robot thinks you said ")
        pprint.pprint(wit_answer)
        text = wit_answer['_text']
        value = wit_answer['entities']['contact'][0]['value']
        if value == "robocik":
            RobotUtils.speak('PL',"Siema!") 
    except sr.UnknownValueError:
        print("Robot could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from WIT AI service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    print("Calibrating!")
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
print("Start listening")
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some unrelated computations for 5 seconds
for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

# calling this function requests that the background listener stop listening
print("Stopping now")
stop_listening(wait_for_stop=False)

# do some more unrelated things
while True: time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping

