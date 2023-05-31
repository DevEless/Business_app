from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    description = models.TextField(max_length=600)

class Project(models.Model):
    titre = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    description = models.TextField(max_length=600)


class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('B', 'Blog'),
        ('P', 'Portfolio'),
    ]

    titre = models.CharField(max_length=30)
    image = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=600)
    content_type = models.CharField(max_length=1, choices=CONTENT_TYPE_CHOICES, default='B')
