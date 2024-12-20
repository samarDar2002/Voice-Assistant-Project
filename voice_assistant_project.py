# -*- coding: utf-8 -*-
"""Voice Assistant Project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qw-SyJTipor3RxMpxWrJESdMBc49F6G2
"""

!pip install gTTS

from gtts import gTTS
from IPython.display import Audio

def speak(text):
    """Convert text to speech."""
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    return Audio("output.mp3", autoplay=True)

# Example usage
speak("Hello! I am your voice assistant.")