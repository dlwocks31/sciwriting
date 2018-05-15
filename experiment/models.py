'''
Models of app `experiment`.
Provides database model `Result`.
'''
from django.db import models

# https://docs.djangoproject.com/en/2.0/ref/models/fields/
class Result(models.Model):
    '''
    Database scheme for experiment result.
    '''
    res_date = models.DateTimeField('Date when experiment is done')
    timetext = models.TextField('Main data of experiment')
    mode = models.BooleanField('True=mode1, False=mode2')
    email = models.CharField('Email of the person', max_length=128)
    is_receive_rep = models.BooleanField('Whether to receive report afterward')
    is_reward = models.BooleanField('Whether to participate in reward chucheom.')
