from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=127, blank=True)

    def __str__(self):
        return f"{self.title} ({self.author})"
