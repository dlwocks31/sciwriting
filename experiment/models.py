'''
Models of app `experiment`.
Provides database model `Result`.
'''
from django.db import models

# https://docs.djangoproject.com/en/2.0/ref/models/fields/
class User(models.Model):
    ipaddr = models.CharField('IP address of the person', max_length=16)
    useragent = models.CharField('User Agent of the person', max_length=256)
    referer = models.CharField('Referer of the person', max_length=128)

class Result(models.Model):
    '''
    Database scheme for experiment result.
    '''
    res_date = models.DateTimeField('Date when experiment is done')
    timetext = models.TextField('Main data of experiment')
    surveyinfo = models.ForeignKey('Survey', on_delete=models.SET_NULL, null=True)

class Survey(models.Model):
    is_receive_rep = models.BooleanField('Whether to receive report afterward')
    is_reward = models.BooleanField('Whether to participate in reward chucheom.')
    email = models.CharField('Email of the person', max_length=128)
    phonenum = models.CharField('Phone number of the person', max_length=20)
