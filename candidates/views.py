from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import Candidate
from .forms import CandidateForm


def index(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)

        if form.is_valid():
            candidate = Candidate(**form.cleaned_data)
            candidate.save()
            return redirect("candidates:index")

    candidates = Candidate.objects.all()
    return render(request, "candidates/index.html", {"candidates": candidates})


def new(request):
    form = CandidateForm()
    return render(request, "candidates/new.html", {"form": form})


def show(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    return render(request, "candidates/show.html", {"candidate": candidate})


def edit(request, id):
    candidate = get_object_or_404(Candidate, id=id)

    if request.method == "POST":
        form = CandidateForm(request.POST)

        if form.is_valid():
            candidate.name = form.cleaned_data["name"]
            candidate.party = form.cleaned_data["party"]
            candidate.age = form.cleaned_data["age"]
            candidate.introduction = form.cleaned_data["introduction"]
            candidate.save()

            return redirect("candidates:show", id=id)

    else:
        form = CandidateForm(candidate.__dict__)

    return render(
        request, "candidates/edit.html", {"form": form, "candidate": candidate}
    )


@require_POST
def delete(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    candidate.delete()
    return redirect("candidates:index")
