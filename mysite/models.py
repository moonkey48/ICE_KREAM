# Create your models here.

from django.db import models


class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


