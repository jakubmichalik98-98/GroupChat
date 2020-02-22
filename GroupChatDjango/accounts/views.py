from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, 'signup.html', {"form": form})


