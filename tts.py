from gtts import gTTS
import os


def Text_to_speech(Message):
    speech = gTTS(text=Message)
    speech.save("tts.mp3")
