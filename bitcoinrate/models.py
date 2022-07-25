from django.db import models

# Create your models here.
class Bitcoinrate(models.Model):
    rate = models.FloatField()