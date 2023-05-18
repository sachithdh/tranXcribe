import os
import openai
from dotenv import load_dotenv

load_dotenv()

def transcribe(audio_file):
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = "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"
    # audio_file = open("audio.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript.text