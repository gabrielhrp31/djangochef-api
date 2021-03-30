from django.db import models

from djangochef.Models.Chef import Chef


class Recipe(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    chef = models.ForeignKey(Chef, null=False, on_delete=models.CASCADE)
