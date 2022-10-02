import pyttsx3

engine = pyttsx3.init()
engine.say("hy, my name is vasu and im using pyttsx3 to run this program")
engine.runAndWait()
engine.stop()