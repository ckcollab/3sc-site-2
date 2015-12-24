from django.db import models


class Applicant(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    essay = models.TextField()
