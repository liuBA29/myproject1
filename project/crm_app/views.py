from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('сТРАНІЦА СРМОЧКІ МОЕЙ')


def contragents(request):
    return HttpResponse('CONTRAGENTS ARE HERE')

def cats(request):
    return HttpResponse('categories')