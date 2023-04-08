import wolframalpha
import wikipedia
import pyttsx3
import speech_recognition as sr
import re
import time
import webbrowser
import smtplib
import requests
import os
from urllib.request import urlopen
import urllib.request
import json

def wolfram_search(query):
    client = wolframalpha.Client("23GQ5G-93H8KH5KXT")
    res = client.query(query)
    try:
        result = next(res.results).text
    except StopIteration:
        result = None
    return result

def wikipedia_search(query):
    try:
        result = wikipedia.summary(query, sentences=3)
    except wikipedia.exceptions.DisambiguationError as e:
        result = "Can you please be more specific?"
    except wikipedia.exceptions.PageError as e:
        result = "Sorry, I could not find any results for that search."
    return result

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def respond(query):
    result = None
    if "wikipedia" in query:
        query = query.replace("wikipedia", "")
        result = wikipedia_search(query)
    elif "search" in query:
        query = query.replace("search", "")
        result = wolfram_search(query)
    elif "open" in query:
        query = query.replace("open", "")
        webbrowser.open(query)
        result = "Opening " + query
    elif "time" in query:
        result = "The current time is " + time.strftime("%H:%M")

    return result

if __name__ == "__main__":
    speak("Hi, how can I assist you?")

    while True:
        query = get_audio()

        if "exit" in query:
            speak("Goodbye!")
            break

        response = respond(query)
        if response:
            speak(response)
        else:
            speak("Sorry, I did not understand that.")
