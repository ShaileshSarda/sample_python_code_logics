"""
1. Text to speech (method - 1)
"""
# pip install gTTS
# pip install playsound
# from gtts import gTTS
# import os
# tts = gTTS(text='Hi, I am from srujan Lab. How may i help you today?', lang='en')
# tts.save("greet.mp3")

from gtts import gTTS
from playsound import playsound
text = 'Hi, I am from srujan Lab. How may i help you today?'
# text = "यह हिंदी में एक उदाहरण है"
var = gTTS(text = text, lang = 'en', tld='co.in')
var.save('eng.mp3')
playsound('.\eng.mp3')

"""
2. Text to speech (method - 2)
"""
'''
#pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
# text = "Hi, I am from srujan Lab. How may i help you today?"
# engine.say(text)
# engine.save_to_file(text, 'test.mp3')
# engine.runAndWait()
# engine.stop()


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 165)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

text = "Hi, I am from srujan Lab. How may i help you today?"
engine.say(text)
engine.save_to_file(text, 'test.mp3')
engine.runAndWait()
engine.stop()
'''
'''
## Change the male and female voice
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voices)
    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''

"""
3. Different Method speech to text
"""
'''
# pip install SpeechRecognition
# pip install pipwin
# pip install pyaudio


# import required module
import speech_recognition as sr


# explicit function to take input commands
# and recognize them
def takeCommandHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        # seconds of non-speaking audio before
        # a phrase is considered complete
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='hi-In')

            # for listening the command in indian english
            print("the query is printed='", Query, "'")

        # handling the exception, so that assistant can
        # ask for telling again the command
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query


# Driver Code

# call the function
takeCommandHindi()
'''