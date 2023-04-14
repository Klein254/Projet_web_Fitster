from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    height = models.IntegerField(blank=True, null=False)
    weight = models.IntegerField(blank=True, null=False)
    age = models.IntegerField(blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)


def __str__(self):
    return self.name
