import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_blog_with_gemini(tone, word_count, prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Write a {tone} blog post of around {word_count} words about: {prompt}.Return output as a valid JSON object with exactly two keys: 'Title' and 'Content'.Do not include any explanations, code fences, or extra text. Only return JSON."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating blog: {str(e)}"
