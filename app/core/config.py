import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# OpenAI API key and base URL
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")