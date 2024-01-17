from django.db import models


class Regex(models.Model):
    name = models.CharField(max_length=50)
    regex = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Regexs'


class FormatJson(models.Model):
    name = models.CharField(max_length=150)
    json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
