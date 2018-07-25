# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(
        verbose_name=("Name"),
        max_length=255,
        # blank=True,
    )

    mark = models.CharField(
        verbose_name=("Mark"),
        max_length=255,
        blank=True,
        null=True
    )