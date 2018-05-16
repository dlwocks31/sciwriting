'''
Models of app `experiment`.
Provides database model `Result`.
'''
from django.db import models

# https://docs.djangoproject.com/en/2.0/ref/models/fields/
class User(models.Model):
    ipaddr = models.CharField('IP address of the person', max_length=16)
    useragent = models.TextField('User Agent of the person')
    referer = models.TextField('Referer of the person')
    firstresult = models.ForeignKey('Result', on_delete=models.SET_NULL, null=True)
    survey = models.ForeignKey('Survey', on_delete=models.SET_NULL, null=True)

class Result(models.Model):
    '''
    Database scheme for experiment result.
    '''
    doneby = models.ForeignKey('User', on_delete=models.CASCADE, name='uid')
    postcnt = models.IntegerField('nth submission(base 0)')
    res_date = models.DateTimeField('Date when experiment is done', name='date')
    data = models.TextField('Main data of experiment', default=r'{}')

class Survey(models.Model):
    is_poster = models.BooleanField('Whether to receive poster afterward', default=False)
    is_lotto = models.BooleanField('Whether to participate in reward lotto.', default=False)
    email = models.CharField('Email of the person', max_length=128, blank=True)
    phone = models.CharField('Phone number of the person', max_length=20, blank=True)
