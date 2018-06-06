from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    tech_used = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
