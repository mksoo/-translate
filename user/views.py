from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user.forms import UserForm

from user.models import UserProfile


def logout_view(request):
    logout(request)
    return redirect("/")


def add_user_profile(req, user):
    name = req['name']
    email = req['email']

    user_profile = UserProfile(user=user, name=name, email=email, created_at=user.date_joined,
                               updated_at=user.date_joined, deleted=False, deleted_at=None)
    user_profile.save()


# userid, name, email, created_at, updated_at, deleted, deleted_at
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        req = request.POST
        if form.is_valid():
            form.save()
            user = User.objects.get(username=req['username'])

            add_user_profile(req, user)

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password) # 사용자 인증

            login(request, user)  # login
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})


def mypage(request):
    return render(request, "user/mypage.html")


def forgot(request):
    return render(request, "user/forgotemail.html")
