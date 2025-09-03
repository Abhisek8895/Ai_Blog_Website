from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


# Register
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

# Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# Profile
@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = user.profile  # one-to-one relation
    return render(request, "users/profile.html", {"user": user, "profile": profile})

@login_required
def edit_profile(request, user_id):
    if request.user.id != user_id:
        messages.error(request, "You can only edit your own profile")
        return redirect("profile", user_id=request.user.id)

    user = get_object_or_404(User, id=user_id)
    profile = user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile", user_id=user.id)
        else:
            messages.error(request, "There was an error updating your profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "users/edit_profile.html", {"form": form})
