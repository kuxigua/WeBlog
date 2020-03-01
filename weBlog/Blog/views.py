from django.forms import model_to_dict
from django.shortcuts import render
from .models import *
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    article = Article.objects.all().order_by('-id')
    article_dict = {"article": article}
    return render(request, 'index.html', context=article_dict)


def ArticleDetail(request):
    article_id = request.GET.get("article_id")
    article_content = Article.objects.get(id=article_id)
    return HttpResponse(article_content.content)