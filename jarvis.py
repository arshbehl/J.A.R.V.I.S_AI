import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    
    elif hour>=16 and hour<21:
        speak("Good Evening!")

    else:
        speak("Good Night!")
 
        
    speak("I am Jarvis. Please tell me, how may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string ouput.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    speak("Hello Sir.")
    WishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'Wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open try hack me' in query:
            webbrowser.open("tryhackme.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        
        elif 'play music' in query:
            music_dir = 'E:\\Arsh\\Mobile Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        

        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\arshb\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to arsh' in query:
            try:
                speak("What should I say sir?")
                content = takeCommand()
                to = "arshbehl1@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")