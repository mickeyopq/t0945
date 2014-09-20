from django.db import models

# Create your models here.
class Pgg(models.Model):
    tel = models.CharField(max_length=15)
    def __unicode__(self):
        return self.tel

class BWH(models.Model):
    name = models.CharField(max_length=30)
    bust = models.CharField(max_length=30)
    waist = models.CharField(max_length=30)
    hips = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name