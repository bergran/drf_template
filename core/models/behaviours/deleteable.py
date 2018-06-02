# -*- coding: utf-8 -*-

from django.db import models


class Deleteable(models.Model):
    deleted = models.BooleanField(default=False)

    objects = models.Manager().from_queryset()