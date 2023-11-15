import os

import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

firebase_url = os.getenv("FIREBASE_URL")


def save_gpt_result(result: str):
    requests.put(
        "https://chatgpt-44d5f-default-rtdb.firebaseio.com/chatgpt_result.json",
        json=result,
    )


def fetch_gpt_result():
    return requests.get(
        "https://chatgpt-44d5f-default-rtdb.firebaseio.com/chatgpt_result.json"
    ).json()
