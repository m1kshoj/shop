from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("main")


def articles(request, article):
    if int(article) > 20:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>article</h1><p>{article}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(
        '<h1>Страница не найдена</h1>')  # функция для вывода понятной пользователю инфы на странице с кодом 404
