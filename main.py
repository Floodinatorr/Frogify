import os
import sys

from model import *
from dotenv import load_dotenv


"""assistant = Assistant("Flood", "tr-TR")
assistant.wait2wake()

a = read_data("model/data/data.csv")
"""

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
model = ChatModel(GEMINI_API_KEY, "en")
question = ""
assistant = Assistant("Flood", "tr-TR")
while True:
    assistant.run(model)
    
    