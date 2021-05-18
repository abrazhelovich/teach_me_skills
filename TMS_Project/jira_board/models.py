from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    prject_id = models.AutoField(primary_key=True)
    key = models.TextField()
    name = models.TextField()


class ProjectField(models.Model):
    name = models.TextField()
    field_id = models.TextField()
