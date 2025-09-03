from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
