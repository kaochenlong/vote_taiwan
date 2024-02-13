from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Candidate


def index(request):
    if request.method == "POST":
        candidate = Candidate(
            name=request.POST["name"],
            party=request.POST["party"],
            age=request.POST["age"],
            introduction=request.POST["introduction"],
        )
        candidate.save()
        return redirect("candidates:index")

    return render(request, "candidates/index.html")


def new(request):
    return render(request, "candidates/new.html")
