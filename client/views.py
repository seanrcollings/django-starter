from django.shortcuts import render


def index(request, path):
    return render(request, "client/index.html")


def other(request):
    return render(request, "client/other.html")