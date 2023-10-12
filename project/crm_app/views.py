from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('сТРАНІЦА СРМОЧКІ МОЕЙ')


def contragents(request):
    return HttpResponse('CONTRAGENTS ARE HERE')

def categories(request, catid):
    return HttpResponse(f"Category:   {catid}")