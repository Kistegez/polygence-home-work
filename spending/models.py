from django.db import models

# Create your models here.

class Spending (models.Model):
    spent_at = models.DateTimeField()
    amount = models.FloatField()
    currency = models.TextField()
    description = models.TextField()
