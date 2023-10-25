from gtts import gTTS
import pygame.mixer
import time

AUDIO_FILE_PATH = 'audio_response.mp3'

def make_audio(phrase):
    tts = gTTS(phrase)
    tts.save(AUDIO_FILE_PATH)

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE_PATH)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
