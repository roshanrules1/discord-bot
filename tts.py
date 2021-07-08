from gtts import gTTS
import os


def Text_to_speech(Message):
    speech = gTTS(text=Message, lang="en", tld="ca")
    speech.save("tts.mp3")
