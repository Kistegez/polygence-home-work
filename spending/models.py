from django.db import models

# Create your models here.

class Spending (models.Model):
    spent_at = models.DateTimeField(auto_now_add=True, blank=True)
    amount = models.FloatField()
    currency = models.TextField()
    description = models.TextField()
