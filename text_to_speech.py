from gtts import gTTS
import pygame.mixer
import time

def speak(phrase):
    tts = gTTS(phrase)
    tts.save('hello.mp3')
    play_mp3('hello.mp3')

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
