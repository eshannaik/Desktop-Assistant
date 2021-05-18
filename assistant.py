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

# global top
# top = Tk()
# top.title("Voice Recognizer")
# top.config(bg="black")

chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
w = webbrowser.get('chrome')
r = sr.Recognizer()

global name
# global greeting
# greeting=["good morning","good afternoon","good evening","good night"]

# Accessing your microphone to listen to your request
my_mic = sr.Microphone()

# Listens to you
def listen():
	while True :
		with my_mic as source:
			print("I am listening")
			audio=r.listen(source,timeout=3)
		try :
			result = r.recognize_google(audio)
			print("Recognizing...") 
		except sr.UnknownValueError:
			print("Google Speech Recognition did not understand the audio")
		except sr.RequestError as e:
			print("Request Failed; {0}".format(e))

			# if "goodbye" in result:
			# 	listening == False
			# else :
		ts(result)

# Finds results for your query
def ts(result1):
	global name,greeting,engine
	result1 = result1.lower()
	# if result1 in greeting:
	# 	engine.say()
	# 	engine.runAndWait()
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

	elif "search for" in result1 or "search" in result1 or "google" in result1 :
		word = result1.replace("search for","")
		word = result1.replace("google","")
		word = result1.replace("search","")
		speak("Searching Google")
		search_google(word)
		speak("Here are some of the results")

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

	elif "open wikipedia" in result1:
		speak("Opening Wikipedia")
		w.open("wikipedia.com")

	elif "where is" in result1 :
		result1 = result1.replace("where is","")
		location = result1
		print(location)
		speak("User asked to locate")
		speak(location)
		w.open("https://www.google.com/maps/place/" + location )

	elif "open calculator" in result1 :
		subprocess.Popen("C:/Windows/System32/calc.exe")

	elif "open notepad" in result1 :
		subprocess.Popen("C:/Windows/System32/notepad.exe")

	# elif "open camera" in result1 or "why am i single" :
	# 	subprocess.Popen("C:/Windows/System32/camera.exe")

	elif "open steam" in result1 :
		speak("Opening Steam")
		os.startfile("D:/Games/Steam/steam.exe")

	elif "my microphones" in result1 or "my micrphone" in result1 :
		speak("Here are the list of microphones")
		microphone_list()

	elif "jokes" in result1 or "joke" in result1 :
		speak(pyjokes.get_joke())

	elif "exit" in result1 or "goodbye" in result1 or "bye" in result1 or "good night" in result1:
		speak("see ya later")
		exit()

	# for fun

	elif "will you be my girlfriend" in result1 or "will you be my gf" in result1 :
		speak("Yes, i would love too!")

	elif "will you be my boyfriend" in result1 or "will you be my bf" in result1 :
		speak("ahhhhhhhhhhhhhhhhhhhh, im a female")

	elif "i love you" in result1 :
		speak("awwwww")

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
	engine.say("Please input your name")
	engine.runAndWait()
	name = input("Enter your name : ")
	name = name.lower()
	engine.say("Hello"+name)
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

greeting()

# def listm():
# 	global l
# 	l = Tk()
# 	l.title("List of microphones in the device")

# 	t = Text(l)
# 	for index, name in enumerate(sr.Microphone.list_microphone_names()):
# 	    t.insert("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# 	l.mainloop()


# bl = Button(top,text="List of microphones in the device",command = listm)
# bl.pack()

# top.mainloop()