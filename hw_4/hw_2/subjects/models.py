from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'ID {self.id}, title: {self.title}'
