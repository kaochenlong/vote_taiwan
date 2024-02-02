from django.shortcuts import render


def index(request):
    return render(request, "candidates/index.html")


def new(request):
    return render(request, "candidates/new.html")
