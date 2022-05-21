from django.db import models
class Payment(models.Model):
    payment_mode = models.CharField(max_length=20)
    amount = models.IntegerField()

# Create your models here.
