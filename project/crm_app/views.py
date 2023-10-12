from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('СТРАНІЦА СРМОЧКІ МОЕЙ')


def contragents(request):
    return HttpResponse('CONTRAGENTS ARE HERE')

def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"Category: {catid}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')