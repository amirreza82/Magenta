import pyttsx3 as px

def Magentainfo(Name,convertor):
    px.speak("Hello" + Name +"Wellcome To Magenta information!")
    F = open("Magenta.txt", "r")
    px.speak(F.read())
    px.speak(Name + "These are the information that they have achieved about me.Do you know any more?")
    User = convertor()
    if "y" in User:
        W = open("User_New1.txt","w")
        px.speak("Ok"+Name+"Now You Can Edit my Information!")
        W.write(convertor())