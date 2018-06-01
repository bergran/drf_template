# -*- coding: utf-8 -*-

from django.db import models


class NameManager(models.QuerySet):
    def named_by(self, name):
        self.filter(name=name)
