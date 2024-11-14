# # Python program to translate
# # speech to text and text to speech


# import speech_recognition as sr
# import pyttsx3

# # Initialize the recognizer
# r = sr.Recognizer()


# # Function to convert text to
# # speech
# def SpeakText(command):

#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()


# # Loop infinitely for user to
# # speak

# while 1:

#     # Exception handling to handle
#     # exceptions at the runtime
#     try:

#         # use the microphone as source for input.
#         with sr.Microphone() as source2:

#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.2)

#             # listens for the user's input
#             audio2 = r.listen(source2)

#             # Using google to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()

#             print("Did you say", MyText)
#             SpeakText(MyText)

#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))

#     except sr.UnknownValueError:
#         print("unknown error occurred")


# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = "Welcome to geeksforgeeks Joe!"

# Language in which you want to convert
language = "en"

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")
