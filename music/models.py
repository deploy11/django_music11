from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=500)
    text = models.TextField()
    musiqa = models.FileField(upload_to='music/')