import os

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL", None)
DEFAULT_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo-0125")
