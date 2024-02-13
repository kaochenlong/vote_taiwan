from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=50)
    age = models.IntegerField()
    introduction = models.TextField()
