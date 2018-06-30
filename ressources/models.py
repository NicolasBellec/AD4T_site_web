from django.db import models
from django.utils import timezone
from media.models import Media

# Create your models here.
class Ressource(models.Model):
    title = models.CharField(max_length = 256)
    title_readable = models.CharField(max_length = 256)
    date = models.DateTimeField(default=timezone.now)
    media = models.OneToOneField(Media, on_delete=models.CASCADE, default=None)
    description = models.CharField(max_length = 500)

    #Tag

    class Meta:
        verbose_name = 'ressource'
        ordering = ['-date']

    def __str__(self):
        return self.title_readable

    def __unicode__(self):
        return self.title_readable
