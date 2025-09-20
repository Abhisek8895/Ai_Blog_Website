# generator/forms.py
from django import forms

class BlogGeneratorForm(forms.Form):
    prompt = forms.CharField(
        label="Blog Topic / Prompt",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Enter a topic or idea..."}),
    )
    word_count = forms.IntegerField(
        label="Word Count",
        min_value=50,
        max_value=2000,
        initial=500,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    tone = forms.ChoiceField(
        label="Tone",
        choices=[
            ("neutral", "Neutral"),
            ("formal", "Formal"),
            ("casual", "Casual"),
            ("technical", "Technical"),
            ("storytelling", "Storytelling"),
        ],
        initial="neutral",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
