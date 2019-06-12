from django.db import models




class isPhishing(models.Model):
    isPhishing = models.BooleanField(default=False)
    rules = models.TextField()
