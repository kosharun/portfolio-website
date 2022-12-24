from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    description_detail = models.TextField(default=" ")
    github_link = models.TextField(default=" ")
    technology = models.CharField(max_length=20)
    image = models.URLField(default=' ')