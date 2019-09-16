from django.db import models
from PIL import Image

# Create your models here.

class Odnosnik(models.Model):
    name = models.CharField(max_length=20)
    link = models.TextField()
    image = models.ImageField(null=False, blank=False, upload_to='odnosniki_pics')

    def __str__(self):
        return self.name