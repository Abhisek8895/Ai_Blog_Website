from django.shortcuts import render
from .forms import BlogGeneratorForm
from .ai_utils import generate_blog_with_gemini
import markdown
from django.utils.safestring import mark_safe
import re

import json

def blog_text_cleaning(blog_output):
    # Remove triple backticks & language markers
    clean_text = re.sub(r"^```[a-zA-Z]*\n|```$", "", blog_output, flags=re.MULTILINE).strip()

    try:
        blog_post = json.loads(clean_text)   # safer than exec
    except json.JSONDecodeError:
        raise ValueError("AI output is not valid JSON")

    # Convert markdown to HTML
    blog_post["Content"] = mark_safe(markdown.markdown(blog_post["Content"]))

    return blog_post

def blog_generator_view(request):
    blog_output = None
    cleaned_blog = None
    if request.method == "POST":
        form = BlogGeneratorForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data["prompt"]
            word_count = form.cleaned_data["word_count"]
            tone = form.cleaned_data["tone"]
            blog_output = generate_blog_with_gemini(tone, word_count, prompt)
            cleaned_blog = blog_text_cleaning(blog_output)
            # print(cleaned_blog)
    else:
        form = BlogGeneratorForm()
    return render(request, "generator/generate_blog.html", {
        "form": form,
        "cleaned_blog": cleaned_blog
    })
