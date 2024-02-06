import pyttsx3

engine = pyttsx3.init()  # Object creation

""" RATE """
rate = engine.getProperty('rate')   # Getting details of the current speaking rate
print(rate)                         # Printing the current voice rate
engine.setProperty('rate', 125)     # Setting up a new voice rate

""" VOLUME """
volume = engine.getProperty('volume')   # Getting to know the current volume level (min=0 and max=1)
print(volume)                          # Printing the current volume level
engine.setProperty('volume', 1.0)      # Setting up the volume level between 0 and 1

""" VOICE """
voices = engine.getProperty('voices')   # Getting details of the current voice
# engine.setProperty('voice', voices[0].id)  # Changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)   # Changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

""" Saving Voice to a file """
# On Linux, make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file("Hello World", "test.mp3")
engine.runAndWait()
