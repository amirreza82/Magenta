#Imported The requirement Module
from Magenta import Magentainfo

from Settings import TheSetting

import pywhatkit

from translate import  Translator

import pywhatkit as pwt

import speech_recognition as sr

import pyttsx3 as px

from AppOpener import run

#This is Convertor Function
#convert Speech To Text
r = sr.Recognizer()
#The Main convertor Function
def convertor():
    try:
        with sr.Microphone() as src:
            audio = r.listen(src)
            text = r.recognize_google(audio)
            text = text.lower()
            return text
    except:
        px.speak("Unfortunately, the conversion attempt was unsuccessful")
#########################################################
#This is a Main Boot Magenta
px.speak("Hello User Whats Your Name?")
User_Name = convertor()
User_Name = User_Name.lower()
User_Name = User_Name.split(" ")
User_Name = User_Name[1]
px.speak("Hello" + User_Name + "How can i Help You?")
#This is loop For repetition boot
while True:
    User = convertor()
    #if True Calling The Setting Module and changed The Boot Settings....
    if "setting" in User:
        TheSetting(User_Name,convertor)
    #This is Condition For Get Information Magenta Boot
    elif "who are you" in User:
        px.speak("I'm magenta 4 days old from Iran ")
        px.speak("Do you want to get more information from me?")
        Users = "Yes"
        Users =convertor()
        users = Users.lower()
        if "y" in User:
            #Calling MagentaInfo Module...
            Magentainfo(User_Name,convertor)
    elif "open application" in User:
        px.speak("Ok,Which program?")
        User_Program = convertor()
        run(User_Program)

            #This is Condition for Search to Google
    elif "search" in User:
            px.speak(User_Name + "What are you going to do?")
            User = convertor()
            pwt.search(User)
            #This is Condition for Search and Play music to youtube...
    elif "Music" in User:
            px.speak(User_Name + 'Please Enter a song or singer Name! ')
            Music_Name = convertor()
            pywhatkit.playonyt(Music_Name)
            #This is Condition for Exit Program....
    elif "Exit" in User:
            px.speak("Good By"+User_Name)
            #break The loop And Exit program...
            break
    elif "translate" in User:
            try:
                px.speak("welcome To Magenta Translator ")
                px.speak("Please Enter a Text Translation")
                user_translate = convertor()
                translator = Translator(to_lang="fe")
                user_translate = translator.translate(user_translate)
                F = open("TrasnlatedFile.txt","w")
                F.write(user_translate)
            except:
                px.speak("Warning Error")
    else:
            px.speak(User_Name+"Unfortunately, I was able to find an item about your request and I am searching for it on Google right now so that you can find similar items on Google. Thanks Magenta.")
            pwt.search(User)




