import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function for greeting user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if (hour ==0 and hour<12):
        speak("Good morning")

    elif(hour<=16 and hour > 12):
        speak("Good Afternoon")
    
    elif(hour<=19 and hour> 16):
        speak("Good Evening")

    else:
        speak("Good Night")

    speak("Hii, I am Jarvis Sir. How can I help you?")


# function for listening & recognizing orders
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= "en-in")
        print(f"User said {query}")

    except Exception as e:
        speak("Sorry I didn't recognize what you say. Please try again")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if True:
        query = takeCommand().lower()

        # for searching in wikipedia
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        # searching anything on google
        elif 'google' in query:
            speak("Searching on google")
            webbrowser.open(f"{query}_google.com")
            

        # for playing video on youtube
        elif 'play video' in query:
            speak("Searching on google")
            webbrowser.open(f"{query} youtube.com")


        # for opening geeksforgeeks website
        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.com")


        # playing song from local directory
        elif 'play music' in query:
            music = "C:\\Users\\Abhishek Kangane\\Music\\Love_Mushups"
            songs = os.listdir(music)
            # fo printing or listing songs
            # print(songs)
            os.startfile(os.path.join(music , songs[0]))

        # for telling the current time
        elif "the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is: {strTime}")

        else:
            print("Stopping...")
            break
