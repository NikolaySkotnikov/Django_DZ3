from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest_articles, name='latest_articles'),
    path('articles/', views.all_articles, name='all_articles'),
    path('articles/<slug:art_slug>/,', views.article_details, name='article'),
]