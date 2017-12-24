from __future__ import unicode_literals
from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=20)


class Notes(models.Model):
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    name = models.CharField(max_length=255)
    nose = models.CharField(max_length=255)
    palate = models.CharField(max_length=255)
    finish = models.CharField(max_length=255)
    extra = models.CharField(max_length=255)


class Names(models.Model):
    name = models.CharField(max_length=255)


class Nose(models.Model):
    nose = models.CharField(max_length=255)


class Palate(models.Model):
    palate = models.CharField(max_length=255)


class Finish(models.Model):
    finish = models.CharField(max_length=255)
