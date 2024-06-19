import pyttsx3 as p
from selenium_web import infow
import speech_recognition as sr
from youTube_web import *
from new_web import *
import randfacts 
from jokes import *
from weather import *
import datetime

engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate',130)

voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("Good morning")
    elif hour>=12 and hour<16:
        return("Good afternoon")
    else:
        return("Good evening")

today_date = datetime.datetime.now()
r = sr.Recognizer()

speak("Hey there!"+ wishme()+ "I'm your voice assistant.")
speak("Today is "+ today_date.strftime("%d") + " of" + today_date.strftime("%B") + " And its currently" +(today_date.strftime("%I") + (today_date.strftime("%M")) + (today_date.strftime("%p"))))
speak("Today's Temperature in Bangalore is " +str(temp())+ " degree celsius" + "and with " + str(des()))
speak("How may I help you today?")

with sr.Microphone() as source:
    r.energy_threshold=10000                     #Increase spectrum of voice 
    r.adjust_for_ambient_noise(source,1.2)       #Cancel background noice
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)             #Converts audio to text
    print(text)
if "what" and "about" and "you" in text:
    speak("i am having a great time here sir")
speak("what can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold=10000                     #Increase spectrum of voice 
    r.adjust_for_ambient_noise(source,1.2)   
    print("listening....")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold=10000                     #Increase spectrum of voice 
        r.adjust_for_ambient_noise(source,1.2)   
        print("listening...")
        audio =  r.listen(source)
        infor =  r.recognize_google(audio)
    print("searching {} in wikipedia".format(infor))
    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)
    input("Press Enter to close the browser...")
    assist.driver.quit()

elif "play" and "video" in text2:
    speak("sure! Please let me know which video would you like to watch on youtube.")
    with sr.Microphone() as source:
        r.energy_threshold=10000                     #Increase spectrum of voice 
        r.adjust_for_ambient_noise(source,1.2)   
        print("listening...")
        audio =  r.listen(source)
        vid =  r.recognize_google(audio)
        print("Playing {} on youtube".format(vid))
        speak("Playing {} on youtube".format(vid))
        assist = music()
        assist.play(vid)
        input("Press Enter to close the browser...")
        assist.driver.quit()
        
elif "news" in text2:
    speak("Sure! Let me read the news for you.")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact"  in text2:
    speak("Sure! ")
    x=randfacts.get_fact()
    print(x)
    speak("Did you know that, " +x)

elif "joke" in text2:
    speak("Sure sir, get ready for some chuckles")
    ar=joke()
    print(ar[0])
    speak(ar[0])
    print(ar[1])
    speak(ar[1])