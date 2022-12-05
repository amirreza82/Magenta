import pyttsx3
import pyttsx3 as px
def TheSetting(Name,convertor):
    engine = pyttsx3.init()
    engine = pyttsx3.init()
    px.speak("Wellcome To Setting" + Name)
    WhTrue = True
    while WhTrue:
        px.speak(Name + "What do you want to change?")
        User_Changes = convertor()
        if "Voice" in User_Changes:
            px.speak("change bot Voice to famale?")
            Voices = convertor()
            voices = engine.getProperty('voices')
            if "famale" in Voices:
                engine.setProperty('voice', voices[1].id)
            elif "Male" in Voices:
                engine.setProperty('voice', voices[0].id)
            else:
                px.Speak(Name + "Your Answer incorrect! ")
            px.speak("Do you want to Break?")
            Breaks = convertor()
            if "y" in Breaks:
                WhTrue = False

        elif "rate" in User_Changes:
            rate = engine.getProperty('rate')  # getting details of current speaking rate
            print(rate)  # printing current voice rate
            px.speak(Name+ " How many rate  change?")
            rate_change = convertor()
            engine.setProperty('rate', rate_change)  # setting up new voice rate
            px.speak("Do you want to Break?")
            Breaks = convertor()
            if "y" in Breaks:
                WhTrue = False
        elif  "volome" in User_Changes :
            volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
            print(volume)  # printing current volume level
            engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
            px.speak("Do you want to Break?")
            Breaks = convertor()
            if "y" in Breaks:
                WhTrue = False
