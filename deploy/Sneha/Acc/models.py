from django.db import models

# Create your models here.

class Acc(models.Model):
    accHolderName = models.CharField('acc_holder_name',max_length=100)
    accBalance = models.FloatField('acc_bal')
    accType = models.CharField('acc_type',max_length=10)


class Meta:
    db_table = "acc"
