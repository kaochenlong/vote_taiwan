from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import Candidate
from .forms import CandidateForm
from django.contrib import messages


def index(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "新增候選人成功！")
            return redirect("candidates:index")

    # candidates = Candidate.objects.all()

    keyword = request.GET.get("keyword")
    if keyword:
        candidates = Candidate.objects.filter(name__icontains=keyword)
    else:
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
        form = CandidateForm(request.POST, instance=candidate)

        if form.is_valid():
            form.save()
            messages.success(request, "更新候選人成功！")

            return redirect("candidates:show", id=id)

    else:
        form = CandidateForm(instance=candidate)

    return render(
        request, "candidates/edit.html", {"form": form, "candidate": candidate}
    )


@require_POST
def delete(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    candidate.delete()
    messages.success(request, "候選人已刪除！")
    return redirect("candidates:index")
