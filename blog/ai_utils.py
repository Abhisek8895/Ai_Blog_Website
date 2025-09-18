import requests
from django.conf import settings

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
HF_HEADERS = settings.HF_HEADERS
def generate_summary(text: str) -> str:
    """A function that takes the post content and summarizes using ai"""
    try:
        response = requests.post(
            API_URL,
            headers=HF_HEADERS,
            json={"inputs": text},
            timeout=60
        )
        response.raise_for_status()
        result = response.json()
        if isinstance(result, list) and len(result) > 0 and "summary_text" in result[0]:
            return result[0]["summary_text"]
        return None
    except requests.exceptions.Timeout:
        print("Hugging Face request timed out. Try again later.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
