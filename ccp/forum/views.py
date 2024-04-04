from django.shortcuts import render


def index(request): #HttpRequest
    return HttpResponse("Страница приложения forum")
    
