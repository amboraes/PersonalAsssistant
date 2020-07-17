# Description: This is a virtual assitant program, that gets the date, current time,
# responds back with a randome greeting and returns information on a person.

# pip instal pyaudio
# pip install SpeachRecognition
# pip install gTTS
# pip install wikipedia

# Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignore any warning messages

warnings.filterwarnings('ignore')


# Fucntion for record audio and return it as a string

def recordAudio():
    # Record the audio
    r = sr.Recognizer()  # Creating a recognizer object

    # open the microphone and start recording
    with sr.Microphone() as source:
        print('Say Something!')
        audio = r.listen(source)
    # Use google speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:  # Check for uknown error
        print('Google speech recognition could not understand the audio, iknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error' + e)
    return data


recordAudio()
