'''
Django models
'''
from django.db import models


# Create your models here.
class List(models.Model):

    """Docstring for List. """

    pass


class Item(models.Model):

    """Item Model"""

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
