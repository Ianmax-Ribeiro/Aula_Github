from django.db import models


class Test01(models.Model):
    Nome = models.CharField(
        max_length=30,
    )
