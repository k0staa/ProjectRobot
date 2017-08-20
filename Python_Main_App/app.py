use_mshield = True

from flask import Flask, render_template, request, redirect, url_for, make_response
import mshield as motors
# import motors
import RPi.GPIO as GPIO
from speaking import SpeakEngine

motors.enable()
speakEngine = SpeakEngine()

app = Flask(__name__) #set up flask server

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #cast changepin to an int

	if changePin == 1:
		motors.turnLeft()
	elif changePin == 2:
		motors.forward()
	elif changePin == 3:
		motors.turnRight()
	elif changePin == 4:
		motors.backward()
                print "backward"
	else:
		motors.stop()


	response = make_response(redirect(url_for('index')))
	return(response)

@app.route('/speak', methods=['POST'])
def speak_in_polish():
	words_to_speak = request.form['words']
	speakEngine.speak_in_polish(words_to_speak)
	response = make_response(redirect(url_for('index')))
	return(response)

@app.route('/speak_english', methods=['POST'])
def speak_in_english():
	words_to_speak = request.form['words']
	speakEngine.speak_in_english(words_to_speak)
	response = make_response(redirect(url_for('index')))
	return(response)


app.run(debug=False, host='0.0.0.0', port=8765) 
motors.disable()
