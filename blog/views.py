from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
