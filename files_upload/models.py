from django.db import models

# Create your models here.

class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='files/')