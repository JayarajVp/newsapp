from django.shortcuts import render
from django.http import JsonResponse
import feedparser
from .models import NewsArticle

def fetch_google_news():
    """Fetch latest Google News and store in the database."""
    rss_url = "https://news.google.com/rss"
    feed = feedparser.parse(rss_url)
    NewsArticle.objects.all().delete()
    for news in feed.entries[:10]:  
        NewsArticle.objects.create(
            title=news.title,
            link=news.link,
            published=news.published
        )
def home(request):
    """Render HTML template."""
    fetch_google_news()  
    return render(request, "newsapp/index.html")
def get_news(request):
    """Return the latest news in JSON format (for AJAX updates)."""
    news = list(NewsArticle.objects.values("title", "link", "published"))
    return JsonResponse(news, safe=False)