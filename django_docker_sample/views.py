from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("<h1>Welcome to Pycharm debugging !!!!!!!!!</h1>")
