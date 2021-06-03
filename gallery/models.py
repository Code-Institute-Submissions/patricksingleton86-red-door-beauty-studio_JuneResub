from django.db import models

# Create your models here.


class Style(models.Model):
    name = models.CharField(max_length=254, null=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
