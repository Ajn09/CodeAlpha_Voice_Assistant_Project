import pyttsx3
import datetime
import wikipedia
import requests
import json
import webbrowser
import os
import subprocess
import pywhatkit as kit
import smtplib
import speech_recognition as sr
sr.__version__
'3.8.1'


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#print(voices[1].id)

author = "Ayan"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def sendEmail(to,mail):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('your email address', 'your password')
#     server.sendmail('your email address', to, mail)
#     server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak (f"Good Morning {author}")

    elif hour>=12 and hour<16:
        speak (f"Good Afternoon {author}")

    else:
        speak (f"Good Evening {author}")


    speak(f"i am Hellona, Your Voice Assistant,   How can i help you today?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        r.pause_threshold = 1.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, show_all=False)
        print(f"User Said {query}")

    except Exception as e:
        print(f"Sorry {author}, Say that again")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    # take_command()
    if 1:
        query = take_command().lower()
        if 'wikipedia' and 'who' in query:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak (results)

        elif 'news' in query:
            speak("news headlines")
            query = query.replace("news","")
            url = "https://newsdata.io/api/1/news?country=lk&apikey=pub_4422684d471a012880ccdcf5c0223da07b658"
            news = requests.get(url).text
            news = json.loads(news)
            art = news['results']
            for results in art:
                print(results['title'])
                speak(results['title'])

                print(results['description'])
                speak(results['description'])
                speak("moving on to the next news")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search browser' in query:
            speak("What do you want to search?")
            search_query = take_command().lower()
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Path to Chrome executable
            webbrowser.get(chrome_path).open(f"https://www.google.com/search?q={search_query}")

        elif 'command prompt' in query:
            os.system('start cmd')

        elif 'file' in query:
            os.system('start explorer')

        elif 'code' in query:
            code_path = "C:\\Users\\Ayanthan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            subprocess.Popen(code_path)

        
        elif 'word' in query:
            code_path = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.exe"
            subprocess.Popen(code_path)

        elif 'music' in query:
            music_dir = 'E:\\Hellona\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            media_player_path = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"
    
        # Open each music file using the media player
            for song in songs:
                subprocess.Popen([media_player_path, os.path.join(music_dir, song)])

        elif 'play youtube' in query:
            speak("what should i want to play in youtube")
            cm = take_command().lower()
            kit.playonyt(f"{cm}")

        elif 'send message' in query:
            speak("who do you want to send message?")
            num = input("Enter Mobile No.")
            speak("what message do you want to send?")
            msg = take_command().lower()
            speak("When do you want to send the message?")
            H = int(input("Enter Hour"))
            M = int(input("Enter Minutes"))
            kit.sendwhatmsg(num, msg, H, M)


            
        # elif 'send mail' in query:
        #     speak("what mail do you want to send?")
        #     mail = take_command().lower()
        #     speak("whom do you want to send?")
        #     to = take_command().lower()
        #     sendEmail(to,mail)