from django.db import models
from django.utils import timezone

# Create your models here.
class Ressource(models.Model):
    title = models.CharField(max_length = 256)
    title_readable = models.CharField(max_length = 256)
    date = models.DateTimeField(default=timezone.now)
    #Tag

    class Meta:
        verbose_name = 'ressource'
        ordering = []

    def __str__(self):
        return self.title_readable

    def __unicode__(self):
        return self.title_readable
