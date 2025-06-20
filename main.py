import os

import speech_recognition as sr
import pyttsx3
import webbrowser
# import openaitest


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        # removing pause threshold because 0.8 sec is by default

        audio = r.listen(source)
        try:
            print("Listening....")
            print("Recognising....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(e)
            return "Some Error Occurred Sorry"


if __name__ == '__main__':
    print('PyCharm')
    say("The Date Isssssssss ")
    sites = [["Youtube", "https://youtube.com"], ["Wikipedia", "https://wikipedia.com"],
             ["Google", "https://google.com"]]
    while True:
        query = takeCommand()
        if query == "None":
            continue
        if "exit" in query.lower():
            say("Goodbye!")
            break

        # for site in sites:
        #     if f"open {site[0]}".lower() in query.lower():
        #         say(f"Opening {site[0]} Buddy...")
        #         webbrowser.open(site[1])
        #
        #         if "open music" in query :
        #             musicPath = "C:\Users\User\Downloads\heat-and-snow-ncs-music-227965.mp3"
        #             os.startfile(musicPath)