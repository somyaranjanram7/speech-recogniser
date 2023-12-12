import ctypes
import os
import subprocess
import time

import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime

import winshell
import wolframalpha
from selenium import webdriver
import webbrowser
import shutil
import smtplib
import wikipedia
from PyDictionary import PyDictionary
import pyjokes

import gpspos
import weather
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    # assname = ("Veronica 2 point 0")
    speak("I am your Assistant Veronica 2 point 0")
    # speak(assname)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice!!! Say that again please")
        speak("Unable to Recognize your voice!!! Say that again please")
        # takeCommand().lower()
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    username()

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "introduce yourself" in query:

            speak("I am veronica. A virtual artificial intelligence."
                    "i'm here to assist you verities of task as my best!!! "
                    "24 hours in a day, 7 days in a week, any time i'm ready for you!!!"
                    "all operations are optimized!!! order me, sir")

        elif "veronica" in query:
            speak("yes sir!!! veronica 1 point o in your service. Order me!!!")

        elif 'take a rest' in query:
            speak("thank you sir!!! have a good day.")
            exit()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'ip address' in query:
            ip=requests.get("https://api.ipify.org").text
            speak("your ip address is "+ip)

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "take screenshot" in query:
            speak("please suggest a name for screenshot file")
            ss=takeCommand().lower()
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{ss}.png")
            speak("i am done sir")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif "write a note" in query:

            speak("What should i write, sir")
            note = takeCommand()
            file = open('veronica.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "play a song" in query:
            speak("which song")
            song=takeCommand().lower()
            kit.playonyt(song)

        elif "tell me about weather" in query:
            speak("about wich city")
            city=takeCommand()
            weather.Gen_report(city)

        elif 'tell a joke' in query:
             My_joke = pyjokes.get_joke(language="en", category="neutral")
             speak(My_joke)

        elif 'forecast the weather' in query:
             speak('about which city')
             city=takeCommand()
             weather.Gen_report(city)


        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir, the time is {strTime}")

        elif "so note" in query:

            speak("Showing Notes")
            file = open("veronica.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=2)
             speak("According to Wikipedia")
             # print(results)
             speak(results)

        elif 'find the meaning' in query:

             speak("Which word do u want to find the meaning sir")
             word = takeCommand()
             dictionary = PyDictionary()
             word_mean = dictionary.meaning(word)
             print(word_mean)
             speak(word_mean)

        elif 'search on google' in query:

            speak("what will i search")
            search_string=takeCommand().lower()
            search_string = search_string.replace(' ', '+')
            browser = webdriver.Chrome('chromedriver')
            for i in range(1):
                matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
            speak(matched_elements)

        elif 'search' in query:

            query = query.replace("search", "")
            # query = query.replace("play", "")
            webbrowser.open(query)

        elif "where is" in query:               #1

            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "what is" in query or "who is" in query:               #1
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif "where we are" in query:
            gpspos.address()

        elif "check instagram profile" in query:
            speak("sir please enter the user name correctly")
            name = input("Enter Username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak("here it is")
            time.sleep(5)

        elif 'send email to' in query:
             try:
                 speak("What should I say?")
                 content = takeCommand()
                 speak("whom i send")
                 to=takeCommand()           #"name@gmail.com"
                 sendEmail(to, content)
                 speak("Email has been sent!")
             except Exception as e:
                 print(e)
                 speak("sorry "
                       "mail can't be send")

        else:
            speak("Sorry!!! Sir i can not help you")
