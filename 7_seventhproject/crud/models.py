from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    time = models.DateTimeField

    def __str__(self):
        return self.title
