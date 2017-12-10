from utils.speaking import SpeakEngine
import requests
import json
from colorama import Fore

class RobotUtils:
   speakEngine = SpeakEngine()
   
   @staticmethod
   def init_speaking():
      speakEngine = SpeakEngine()

   @classmethod
   def speak(cls,language, words):
      print("Speaking method" + language)
      if(language == 'PL'):
         cls.speakEngine.speak_in_polish(words)
      else:
         cls.speakEngine.speak_in_english(words)

   @classmethod
   def what_about_chuck(cls):
      try:
         site= "https://api.chucknorris.io/jokes/random"
         hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
         response = requests.get(site, headers=hdr)

         if response.status_code == 200:
            chuck_json = json.loads(response.content.decode('utf-8'))
         else:
            chuck_json = None
         chuck_fact = chuck_json["value"]
         print(Fore.RED + chuck_fact + Fore.RESET)
         cls.speakEngine.speak_in_english(chuck_fact)
      except Exception as e:
            cls.speakEngine.speak_in_english("Looks like Chuck broke the Internet.")
            print(Fore.RED + "Looks like Chuck broke the Internet..." + str(e) + Fore.RESET)

   @staticmethod
   def todo():
      todoHandler(data)

   @staticmethod 
   def movies():
      try:
          movie_name = raw_input(Fore.RED + "What do you want to watch?\n" + Fore.RESET)
      except:
          movie_name = input(Fore.RED + "What do you want to watch?\n" + Fore.RESET)
          system("ims " + movie_name)

   @staticmethod
   def music():
      play(data)

   @staticmethod
   def hotspot_start():
      system("sudo ap-hotspot start")

   @staticmethod
   def hotspot_stop():
      system("sudo ap-hotspot stop")

  
