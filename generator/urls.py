from django.urls import path
from . import views

urlpatterns = [
    path("generate_form/", views.blog_generator_view, name="generate_blog"),
]
