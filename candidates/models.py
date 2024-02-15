from django.db import models
from django.utils import timezone


class CandidateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=50)
    age = models.IntegerField()
    introduction = models.TextField()
    deleted_at = models.DateTimeField(null=True)

    objects = CandidateManager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name} ({self.party})"
