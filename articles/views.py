from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from articles.forms import ArticleForm
from articles.models import Article, Category


def articles_list(request: HttpRequest) -> HttpResponse:
    articles_list = Article.objects.all()

    return render(request, "articles/list.html", {"articles": articles_list})


def article_detail(request: HttpRequest, id: int) -> HttpResponse:
    article = Article.objects.get(id=id)
    return render(request, "articles/detail.html", {"article": article})


def article_create(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if not form.is_valid():
            raise ValueError()
        form.save()
        return redirect("article_list")
    categories = Category.objects.all()
    return render(request, "articles/create.html", {"categories": categories})
