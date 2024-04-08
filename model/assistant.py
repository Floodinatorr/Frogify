
import speech_recognition as sr
import pyttsx3 as tts

class Assistant:
    def __init__(self, name, language="en-US"):
        self.name = name
        self.language = language
        self.engine = tts.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_response(self, request):
        print(f"Hello! My name is {self.name}. How can I help you?")

    def run(self, model):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...", end="")
            audio = r.listen(source)
            try:
                print("Processing...")
                text = r.recognize_google(audio, language=self.language)
                print("You: ", text)
                response = model.ask(text + "Kısaca lütfen, maksimum 50 kelime.")
                print("Model: ", response.text)
            except Exception as err:
                print("Sorry, I did not understand that. Exception: ", err)
