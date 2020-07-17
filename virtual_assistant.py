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


# Function to get the virtual assistant response
def assistantResponse(text):
    print(text)

    # Convert the text to speech

    myobj = gTTS(text=text, lang='en', slow=False)

    # save the converted audio to a file
    myobj.save('assistant_response.mp3')

    # Play the converted file
    os.system('start assistant_response.mp3')


# create a function for wake words or phrase
def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'okay computer']  # List of wake words

    text = text.lower()  # Converting the text to all lower case words

    # Check to see if the user command/text contains a wake word/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    # If the wake word isn't found in the text from the loop and so it returns false
    return False


# A function to get the current date
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # eg Friday
    montNum = now.month
    dayNum = now.day

    # A list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December']
    # A list of ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th'
        , '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21th'
        , '22th', '23th', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31th']

    return 'Today is ' + weekday + ' ' + month_names[montNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'


# A function to return a random greeting response
def greeting(text):
    # Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'greetings', 'hola', 'wassup', 'hello']

    # Greeting responses
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']

    # If the user input is a greeting, then retunr a randomly chosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    # If no greetin was detected then return an empty string
    return ''


# Function to get persons first and last name from the text
def getPerson(text):
    wordList = text.split()  # Splitting the tex into a list of words

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]


while True:
    # Recor the audio
    text = recordAudio()
    response = ''

    # Check for the wake word/phrase
    if (wakeWord(text) == True):
        # Check for greetings by user
        response = response + greeting(text)

        # Check to see if the user said anything having to do with the date
        if 'date' in text:
            get_date = getDate()
            response = response + ' ' + getDate()

        # Check to see if the user said anything to do with the time
        if 'time' in text:
            now = datetime.datetime.now()
            meridiem = ''
            if(now.hour >= 12):
                meridiem = 'p.m' # Post meridiem (PM) after midday
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
                hour = now.hour

            # Convert minute into a proper string
            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' ' + 'It is '+str(hour)+':'+minute+' '+meridiem+'.'
        # Check to see if user said 'who is'
        if 'who is' in text:
            persons = getPerson(text)
            wiki = wikipedia.summary(persons, sentences=2)
            response = response + ' ' + wiki

        # Have the assistant respond back using audio and the text from response
        assistantResponse(response)
