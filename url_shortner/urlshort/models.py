from django.db import models

# Create your models here.

class ShortURL(models.Model):
    long_url = models.URLField(max_length=1000)
    short_url = models.CharField(max_length=100)
    def __str__(self):
        return self.long_url