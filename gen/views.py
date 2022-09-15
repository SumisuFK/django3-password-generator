from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'gen/home.html')


def password(request):
    characters = list("qwertyuiopasdfghjklzxcvbnm")

    if request.GET.get("uppercase"):
        characters.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))

    length = int(request.GET.get("length", 5))

    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'gen/password.html', {'password': thepassword})

def about(request):
    return render(request, "gen/about.html")
