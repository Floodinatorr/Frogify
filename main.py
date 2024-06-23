# 1. Wait for wake word
# 2. Get prompt from user
# 3. Chatbot response
# 4. Paragraph-to-sentences
# 5. Sentiment analysis
# 6. Send animations to the robot
# 7. Speech

# Imports

import os
import sys
import time
import pickle
import datetime

# Load the models

emotion_model = pickle.load(open('models/emotion-model.sav', 'rb'))

# Functions

def predict_emotion(text):
    return emotion_model.predict([text])[0]

# Main
