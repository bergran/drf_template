# -*- coding: utf-8 -*-

from django.db import models


class OnwerManager(models.QuerySet):
    def ownered_by(self, owner):
        self.filter(owner__username=owner)
