from django.db import models
from django.utils import timezone

# Create your models here.
class Profil(models.Model):
    #user = models.OneToOneField(User)

    name = models.CharField(max_length = 256)
    lastname = models.CharField(max_length = 256)
    #poles = models.

    date = models.DateTimeField(default = timezone.now)


    class Meta:
        verbose_name = "profil"
        ordering = ['date']

    def __str__(self):
        return ""

    def __unicode__(self):
        return ""
