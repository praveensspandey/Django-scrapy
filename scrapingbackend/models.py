from django.db import models

# Create your models here.

class Scrap(models.Model):
    title=models.CharField(max_length=150)
    year=models.DecimalField(max_digits=1000, decimal_places=2,null=True)