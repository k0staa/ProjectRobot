import pyttsx3
class SpeakEngine:
	
	def __init__(self):
		self._engine = pyttsx3.init()
		self._engine.setProperty('volume',0.9)
		self._rate = self._engine.getProperty('rate')
		self.speak_in_english(("Hi, this is robot. Speaking module is working."))
		self._engine.runAndWait()

	def speak_in_polish(self,words):
		self._engine.setProperty('voice', 'polish')
		rate = self._rate - 30
		self._engine.setProperty('rate', rate);
		self._engine.say(words)
		self._engine.runAndWait()

	def speak_in_english(self,words):
		self._engine.setProperty('voice', 'english')
		rate = self._rate
		self._engine.setProperty('rate', rate);
		self._engine.say(words)
		self._engine.runAndWait()


