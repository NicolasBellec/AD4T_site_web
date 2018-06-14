from django.db import models

# Create your models here.
class Media(models.Model):
    slug = models.SlugField(max_length=100)
    path = models.FileField(max_length=256)
    content_type = models.CharField(max_length=256)
    permission = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'media'
        ordering = ['content_type']
