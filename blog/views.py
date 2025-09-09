from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import PostForm
from .models import Post, Category
from comments.forms import CommentForm

def home(request):
    posts = Post.objects.all().order_by("-created_at")
    categories = Category.objects.all()
    return render(request, "blog/home.html", {"posts": posts, "categories":categories})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, "blog/home.html", {"posts": posts, "categories": categories, "active_category": category.slug})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-created_at")  # latest first

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "form": form},
    )

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Check if logged-in user is the author
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/edit_post.html", {"form": form, "post": post})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Check if the logged-in user is the author
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == "POST":
        # Delete the post
        post.delete()
        # Redirect to homepage (or profile page if you prefer)
        return redirect("home")

    # If GET request → show confirmation page
    return render(request, "blog/delete_post.html", {"post": post})


@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user in post.likes.all():
        post.likes.remove(request.user)  # unlike
    else:
        post.likes.add(request.user)     # like

    return redirect("post_detail", slug=slug)