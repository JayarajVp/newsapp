from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=225)
    link = models.URLField()
    published = models.CharField(max_length=222)

    def __str__(self):
        return self.title
    
