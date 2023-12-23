import speech_recognition as sr
import win32com.client
import webbrowser
import wikipedia
import datetime
import pyaudio
import openai
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# function for greeting user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if (hour > 0 and hour<12):
        speaker.Speak("Good morning")

    elif(hour<=16 and hour > 12):
        speaker.Speak("Good Afternoon")
    
    elif(hour<=19 and hour> 16):
        speaker.Speak("Good Evening")

    else:
        speaker.Speak("Good Night")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print((f"User Said : {query}"))
            return query
        except:
            return "Sorry, some error occured."


if __name__=='__main__':
    wishMe()
    speaker.Speak("Hello I am Jarvis A.I. Sir, How can I help You?")
    count = 0
    while (count < 10):
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["DSA Profile","https://leetcode.com/kanganeabhishek2002/"],
                 ["instagram", "https://instagram.com"], ["linkedin","https://www.linkedin.com/in/abhishek-kangane-4ba933242/"],
                 ["geeks for geeks","https://auth.geeksforgeeks.org/user/abhikangane1392"],]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
        
        # playing song from local directory
        if 'play music' in query.lower():
            speaker.Speak("Playing music from local directory")
            music = "C:\\Users\\Abhishek Kangane\\Music\\Love_Mushups"
            songs = os.listdir(music)
            os.startfile(os.path.join(music , songs[0]))

        # for searching in wikipedia
        elif 'wikipedia' in query.lower():
            speaker.Speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speaker.Speak("According to wikipedia")
            print(results)
            speaker.Speak(results)

        # searching anything on google
        elif 'google' in query.lower():
            speaker.Speak("Searching on google")
            webbrowser.open(f"{query}.com")

        # for telling the current time
        elif "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speaker.Speak(f"Sir the time is {hour} hour {min} minutes")

        # opening eclipse
        elif "open eclipse" in query.lower():
            eclipsePath = "C:\\Users\\Abhishek Kangane\\eclipse\\java-2022-063\\eclipse\\"
            os.startfile(eclipsePath)

        count = count+1
