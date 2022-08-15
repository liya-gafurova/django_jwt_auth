from django.urls import path
from rest_framework.routers import DefaultRouter

from blog.views import ArticleViewSet

article_router = DefaultRouter()
article_router.register(r'articles',viewset=ArticleViewSet, basename='articles')

blog_urlpatterns = [
    *article_router.urls,

]