from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from user.forms import UserForm


def logout_view(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password) # 사용자 인증

            login(request, user) # login
            return redirect("/")
    else:
        form = UserForm()
    return render(request, "user/register.html", {"form": form})


def mypage(request):
    return render(request, "user/mypage.html")


def forgot(request):
    return render(request, "user/forgotemail.html")
