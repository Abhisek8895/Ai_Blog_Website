import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_blog_with_gemini(tone, word_count, prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Write a {tone} blog post of around {word_count} words about: {prompt}. Return output as a Python dictionary with keys 'Title' and 'Content'.'Title' should contain only the blog title.'Content' should contain the blog body without repeating the title."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating blog: {str(e)}"
