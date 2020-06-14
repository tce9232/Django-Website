import datetime

from django.db import models
from django.utils import timezone

class Contributor(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()