from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

def signup(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, 'signup.html', {"form": form})


