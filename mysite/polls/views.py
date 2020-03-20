from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, its my first django page.")
