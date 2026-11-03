from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from articles.models import Article


def articles_list(request: HttpRequest) -> HttpResponse:
    articles_list = Article.objects.all()

    return render(request, "articles/list.html", {"articles": articles_list})


def article_detail(request: HttpRequest, id: int) -> HttpResponse:
    article = Article.objects.get(id=id)
    return render(request, "articles/detail.html", {"article": article})
