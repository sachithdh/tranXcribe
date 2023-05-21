import os
import openai
from dotenv import load_dotenv

load_dotenv() # load environment variables from a .env file

# Transcribe audio file
def transcribe(audio_file):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript.text
