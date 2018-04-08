from django.db import models
from django.utils import timezone

# Create your models here.
class Passes(models.Model):
    title = models.CharField(max_length = 256)
    title_readable = models.CharField(max_length = 256)
    date = models.DateTimeField(default = timezone.now)
    description = models.TextField(max_length = 20000)
    #Tags
    class Meta:
        verbose_name = "passes"
        ordering = ['date']

    def __str__(self):
        return self.title_readable

    def __unicode__(self):
        return self.title_readable
