from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    tech_used = models.TextField(max_length=300)
    live_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name