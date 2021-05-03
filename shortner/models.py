from django.db import models

# Create your models here.
class Url(models.Model):
    title = models.CharField(max_length=5000)
    uuid = models.CharField(max_length=15)

    def __str__(self):
        return self.title
