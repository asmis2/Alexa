import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as wb
import csv
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 140
engine.setProperty('rate',newVoiceRate)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:

            print("listening..")
            listener.pause_threshold = 1
            talk("Welcome back Mam.. Alexa at your service...How can i help you? ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)


    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif "who is" in command:
        person = command.replace("who is", '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "tell me about" in command:
        thing = command.replace("tell me about", '')
        info1 = wikipedia.summary(thing, 2)
        print(info1)
        talk(info1)

    elif "are you dead" in command:
        talk("No I am alive.")

    elif "date" in command:
        year =int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        talk("The current date is" )
        talk(date)
        talk(month)
        talk(year)

    elif "are you single" in command:
        talk("No I am in a relationship with Jarvis")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "logout" in command:
        os.system("shutdown - l")

    elif "shutdown" in command:
        os.system("shutdown /s /t 1")

    elif "restart" in command:
        os.system("shutdown /r /t 1")

    elif "offline" in command:
        quit()

    else:
        talk("please say the command again..")


while True:
    run_alexa()
