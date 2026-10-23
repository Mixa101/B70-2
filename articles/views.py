from django.http.response import HttpResponse


def hello_world(request):
    return HttpResponse("asd")


def hello_name(request, name):
    return HttpResponse(f"Hello <h1>{name}</h1>!")
