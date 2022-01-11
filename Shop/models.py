from django.db import models
from django.utils import timezone


class Price(models.Model):
    currency = models.CharField(max_length=255) # здесь лучше еще модельку сделать
    value = models.DecimalField(max_length=12, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.value} {self.currency}'

class Type(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    barcode = models.PositiveIntegerField()
    update_date = models.DateField(default=timezone.now)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Currency(models.Model):

#     name = models.CharField(max_length=50)
