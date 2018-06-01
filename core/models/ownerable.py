# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Authorable(models.Model):
    author = models.ForeignKey(User)

    class Meta:
        abstract = True
