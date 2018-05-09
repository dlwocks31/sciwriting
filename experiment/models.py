from django.db import models

class Result(models.Model):
    res_date = models.DateTimeField('date when experiment is done')
# Create your models here.
