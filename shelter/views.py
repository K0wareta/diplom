from django.shortcuts import render
from django.http import HttpResponse
from shelter.models import Animal



def index(request):
    return render(request, "index.html")


def animals(request):
    all_animals = Animal.objects.all()
    return render(request, "animals.html",  context={'data': all_animals})


def contacts(request):
    return render(request, "contacts.html")