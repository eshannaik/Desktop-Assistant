# Virtual Assistant Violet


import speech_recognition as sr # access the microphone
import pyttsx3 # convert text to speech
from tkinter import * # GUI
import datetime 
from datetime import date
import webbrowser #access web browser
import subprocess #call system processes
import os # call non system processes
from googlesearch import search #search google
import pyjokes #jokes
import winshell #empty recycle bin
import pyowm # weather
import smtplib #send email
import time as ti # to stop the virtual assistant from listening
from urllib.request import urlopen #for news
import json
from playsound import playsound #alarm




#Please change path to your browser

chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
w = webbrowser.get('chrome')
r = sr.Recognizer()

global name

# Accessing your microphone to listen to your request
my_mic = sr.Microphone()

# Listens to you
def listen():
	while True :
		with my_mic as source:
			print("I am listening")
			audio=r.listen(source)
		try :
			result = r.recognize_google(audio)
			print("Recognizing...") 
			print(result)
			ts(result)
		except sr.UnknownValueError:
			print("Google Speech Recognition did not understand the audio")
		except sr.RequestError as e:
			print("Request Failed; {0}".format(e))

# Finds results for your query 
# The main function
def ts(result1):
	global name,greeting,engine
	result1 = result1.lower()

	if "hello" in result1 :
		wishme()

	elif "time" in result1 :
		c_t = time()
		speak(f"the current time is{c_t}")

	elif "date" in result1 :
		d = t_date()
		speak(d)

	elif "how are you" in result1 :
		speak("i am doing well. kinda bored though")

	elif "who created you" in result1:
		speak("I was created by eshan as a mini project")

	elif "who are you" in result1:
		speak("I am a virtual assistant made by eshan")

	elif "who am i" in result1:
		speak("If your talking your most probably a human")

	elif "search for" in result1 or "search" in result1 or "google" in result1 :
		word = result1.replace("search for","")
		word = result1.replace("google","")
		word = result1.replace("search","")
		speak("Searching Google")
		search_google(word)
		speak("Here are some of the results")

	elif "open google" in result1:
		speak("Opening Google Chrome")
		w.open("google.com")

	elif "open youtube" in result1 :
		speak("Opening youtube")
		w.open("youtube.com")

	elif "open spotify" in result1 :
		speak("Opening spotify")
		w.open("open.spotify.com")

	elif "open instagram" in result1 :
		speak("Opening instagram")
		w.open("instagram.com")

	elif "open facebook" in result1 :
		speak("Opening facebook")
		w.open("facebook.com")

	elif "open whatsapp" in result1 :
		speak("Opening whatsapp web")
		w.open("web.whatsapp.com")

	elif "open quora" in result1 :
		speak("Opening quora")
		w.open("quora.com")

	elif "open stackoverflow" in result1 :
		speak("Opening stackoverflow")
		w.open("stackoverflow.com")

	elif "open pinterest" in result1 :
		speak("Opening pinterest")
		w.open("pinterest.com")

	elif "open wikipedia" in result1:
		speak("Opening Wikipedia")
		w.open("wikipedia.com")

	elif "open reddit" in result1:
		speak("Opening Reddit")
		w.open("reddit.com")

	elif "open twitter" in result1:
		speak("Opening Twitter")
		w.open("twitter.com")

	elif "where is" in result1 :
		result1 = result1.replace("where is","")
		location = result1
		print(location)
		speak(f"User asked to locate {location}")
		w.open("https://www.google.com/maps/place/" + location )

	elif "open calculator" in result1 :
		subprocess.Popen("C:/Windows/System32/calc.exe")

	elif "open notepad" in result1 :
		subprocess.Popen("C:/Windows/System32/notepad.exe")

	elif "open camera" in result1 or "why am i single" in result1 :
		speak("Opening Camera")
		subprocess.run("start microsoft.windows.camera:", shell =True)

	elif "open steam" in result1 :
		speak("Opening Steam")
		os.startfile("D:/Games/Steam/steam.exe")

	elif "instructions" in result1 or "instruction" in result1 :
		speak("Opening instructions")
		os.startfile("instructions.txt")

	elif "empty recycle bin" in result1:
		speak("Emptying the recycle bin")
		winshell.recycle_bin().empty(confirm=True,show_progress=True,sound=False)
		speak("The recycle bin is empty")

	elif "my microphones" in result1 or "my micrphone" in result1 :
		speak("Here are the list of microphones")
		microphone_list()

	elif "jokes" in result1 or "joke" in result1 :
		speak(pyjokes.get_joke())

	elif "what is today's weather" in result1 or "weather" in result1 :
		speak("Weather of which place")
		location = l()
		speak("Getting weather for ")
		speak(location)

		api_key = '32 bit key'
		openmap = pyowm.OWM(api_key)
		wm = openmap.weather_manager()
		lo = wm.weather_at_place(location)
		data = lo.weather

		speak("the weather is printed on the cmd")

		speak("Do you want me to read out the weather yes or no")
		x = l()

		temp = data.temperature(unit = "celsius")
		rt=time()
		s=data.status
		ds = data.detailed_status

		print("The current time is :", rt)
		print("The temperature currently is : ", temp['temp'])
		print("Will there be clouds :", s)
		print("Will there be clouds :", ds)

		if x=="yes" :
			speak(f"The current weather report at time {rt} is")
			speak(f"temperature {temp['temp']}")
			speak(f"status {s}")
			speak(f"detailed status {ds}")

	elif "send mail" in result1 or "send email" in result1:
		try:
			speak("What should i send?")
			content = l()
			speak("please write the email address i need to send this to on the cmd")
			to= input("Enter email address :")
			send_mail(to,content)
			speak("Email has been sent !")
		except Exception as e:
			print(e)
			speak("Could not send email")

	elif "news" in result1:
		jsonObj = urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=YOUR API KEY')
		data = json.load(jsonObj)
		i=1

		speak("do you want me to read out the news yes or no")
		x=l()

		speak("here are some top news from the times of india")
		print('''=============== TIMES OF INDIA ============'''+ '\n')
		
		try:		 
			for item in data['articles']:
				print(str(i) + '. ' + item['title'] + '\n')
				print(item['description'] + '\n')
				i += 1
		except Exception as e:
			print(str(e))

	elif "alarm" in result1:
		speak("do you want to set the alarm soon (yes or no)")
		x = l()

		if x == "yes":
			speak("In how many seconds do you want the alarm to ring")
			a=int(l())
			ti.sleep(a)
			playsound("alarm_beep.mp3")
		else :
			speak("please input when you want to set the alarm")
			x1 = input("Enter time in Hour(24):Minute format")
			f = True
			while f == True:
				standard_time = datetime.now().strftime("%H:%M")
				if x1 == standard_time:
					playsound("alarm_beep.mp3") 
					f==Flase
			

	elif "don't listen" in result1 or "stop listening" in result1 or "send a mail" in result1:
		speak("For how many seconds do you want me to stop listening")
		a = int(l())
		ti.sleep(a)

	elif "exit" in result1 or "goodbye" in result1 or "bye" in result1 or "good night" in result1:
		speak("see ya later")
		exit()

	elif "shutdown system" in result1:
		speak("Shutting down system")
		subprocess.call('shutdown/p/f')

	# for fun
	# Most asked questions from google assistant
	elif "will you be my girlfriend" in result1 or "will you be my gf" in result1 :
		speak("hmmmmmmmmmmmmmmmm I'll need some time")

	elif "will you be my boyfriend" in result1 or "will you be my bf" in result1 :
		speak("ahhhhhhhhhhhhhhhhhhhh, im a female")

	elif "i love you" in result1 :
		speak("awwwww")

	# contact me
	elif "contact your maker" in result1 or "contact eshan" in result1 or "who is eshan" in result1:
		speak("Here are all the ways to contact my owner")
		w.open("https://github.com/eshannaik")


#listening
def l():
	with my_mic as s:
			print("I am listening")
			au=r.listen(s)
	try :
		query = r.recognize_google(au)
		print("Recognizing...") 
		print(query)
	except sr.UnknownValueError:
		print("Google Speech Recognition did not understand the audio")
	except sr.RequestError as e:
		print("Request Failed; {0}".format(e))

	return query


# A greeting
def greeting():
	global engine
	engine = pyttsx3.init()
	v = engine.getProperty('voices')
	r = engine.getProperty('rate')
	engine.setProperty('rate',150)
	engine.setProperty('voice',v[1].id)
	engine.say("Hello my name is Violet! How can i help you?")
	engine.runAndWait()
	listen()

# Greeting
def wishme():
	global name,engine
	engine.say("Hey what is your name")
	engine.runAndWait()
	name = l()
	name = name.lower()
	engine.say("Nice to meet you"+name)
	engine.runAndWait()

#Speaks	
def speak(text):
	global engine
	engine.say(text)
	engine.runAndWait()

#current time
def time():
	c_t = datetime.datetime.now().strftime("%I:%M %p")
	return c_t

#current date
def t_date():
	d = date.today()
	return d

#list micrphones your system has
def microphone_list():
	for index, name in enumerate(sr.Microphone.list_microphone_names()):
		print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

#searches google for results
def search_google(query):
	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		print(j)

# Enable low security in gmail
def send_mail(to,content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()

	server.login("abc@gmail.com","Password@123")
	server.sendmail("abc@gmail.com",to,content)
	server.close()


greeting()
