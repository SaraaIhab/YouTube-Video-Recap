import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from embedchain import App
from youtube_transcript_api import YouTubeTranscriptApi 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

app = App()

ytt_api = YouTubeTranscriptApi()

def get_transcript(video_id):
  full_text=""
  transcript=ytt_api.fetch(video_id)

  for snippet in transcript:
    full_text+=snippet.text+" "
  
  return full_text

def add_transcript_to_app(video_id):
    transcript = get_transcript(video_id)
    if (transcript==""):
        return "Please enter a valid YouTube ID"
    app.add(transcript)
    return "Transcript added to knowledge base"
