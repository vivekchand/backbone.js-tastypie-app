from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    release_date = models.CharField(max_length=10)

