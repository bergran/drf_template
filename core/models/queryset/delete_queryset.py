# -*- coding: utf-8 -*-

from django.db import models


class DeleteQuerySet(models.QuerySet):
    def is_deleted(self):
        self.filter(deleted=True)
