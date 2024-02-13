from django.shortcuts import render, redirect, get_object_or_404
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

    candidates = Candidate.objects.all()
    return render(request, "candidates/index.html", {"candidates": candidates})


def new(request):
    return render(request, "candidates/new.html")


def show(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    return render(request, "candidates/show.html", {"candidate": candidate})
