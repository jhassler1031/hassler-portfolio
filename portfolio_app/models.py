from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    tech_used = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)
