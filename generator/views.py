# generator/views.py
from django.shortcuts import render
from django.conf import settings
import requests
from .forms import BlogGeneratorForm

HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HF_HEADERS = {"Authorization": f"Bearer {settings.HF_API_TOKEN}"}

def generate_blog_from_prompt(prompt, word_count=500, tone="neutral"):
    """Call Hugging Face API to generate blog content."""
    query = f"Write a {tone} blog post of around {word_count} words about: {prompt}"
    
    try:
        response = requests.post(
            HF_API_URL,
            headers=HF_HEADERS,
            json={"inputs": query},
            timeout=60
        )
        response.raise_for_status()
        result = response.json()
        return result[0]["generated_text"] if isinstance(result, list) else None
    except Exception as e:
        print("Error generating blog:", e)
        return None


def blog_generator_view(request):
    """Handle form submission and generate blog preview."""
    generated_blog = None

    if request.method == "POST":
        form = BlogGeneratorForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data["prompt"]
            word_count = form.cleaned_data["word_count"]
            tone = form.cleaned_data["tone"]

            generated_blog = generate_blog_from_prompt(prompt, word_count, tone)
    else:
        form = BlogGeneratorForm()

    return render(request, "generator/generate_blog.html", {
        "form": form,
        "generated_blog": generated_blog,
    })
