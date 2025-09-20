from django.urls import path
from . import views

urlpatterns = [
    path("", views.generate_blog_view, name="generate_blog"),
]
