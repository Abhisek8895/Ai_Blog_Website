from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("<slug:slug>/edit/", views.edit_post, name="edit_post"),
    path("<slug:slug>/delete/", views.delete_post, name="delete_post"),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path("post/<slug:slug>/like/", views.like_post, name="like_post"),
]
