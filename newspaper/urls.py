from django.urls import path
from .views import home, get_news

urlpatterns = [
    path("", home, name="home"),
    path("get_news/", get_news, name="get_news"),  
]
