import sys
import threading
import tkinter as tk

import speech_recognition as sr
import pyttsx3 as tts

class Assistant:
    def __init__(self, name):
        self.name = name

    def get_response(self, request):
        print(f"Hello! My name is {self.name}. How can I help you?")

    def wait2wake(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...", end="")
            audio = r.listen(source)
            try:
                print("Processing...")
                text = r.recognize_google(audio, language='tr-TR')
                print(f"You said: {text}")
            except Exception as err:
                print("Sorry, I did not understand that. Exception: ", err)
