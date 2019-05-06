from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def preview(self):
        return self.body[:50]

    def created_at_to_str(self):
        date_format = '%Y년 %m월 %d일 %H시 %M분'

        return self.created_at.strftime(date_format)

    def updated_at_to_str(self):
        date_format = '%Y년 %m월 %d일 %H시 %M분'

        return self.updated_at.strftime(date_format)
