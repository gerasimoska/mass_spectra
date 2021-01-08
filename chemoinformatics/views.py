from django.shortcuts import render, redirect


def about(request):
    return render(request, "batch/about.html")


def search(request):
    return redirect("/search")
