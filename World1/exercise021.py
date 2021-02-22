# Exercise 021: PLaying a MP3
# Make a program in Python that opens and executes the audio of an MP3 file

from pygame import mixer
from time import sleep
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
sleep(120)
