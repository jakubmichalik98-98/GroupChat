from django.http import HttpResponse


def index(request):
    return HttpResponse("Witamy w aplikacji do logowania")


