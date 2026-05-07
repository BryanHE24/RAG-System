import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# get environment variable by name
def get_env_variable(name: str) -> str:
    value = os.getenv(name)

    # raise error if environment variable is not set
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")

    return value

# OpenAI API key and base URL
OPENAI_API_KEY = get_env_variable("OPENAI_API_KEY")
OPENAI_BASE_URL = get_env_variable("OPENAI_BASE_URL")