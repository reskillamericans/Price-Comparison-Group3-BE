# Framework for Price Comparison tool

from django.db import models


# Create Models


class Price(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __float__(self):
        return self.cost


class Description(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class AdditionalInfo(models.Model):
    class Meta:
        verbose_name_plural = "Additional Info"
    text = models.CharField(max_length=3000)

    def __str__(self):
        return self.text


class ProductName(models.Model):
    name = models.CharField(max_length=400)
    price = models.ForeignKey(Price, blank=True, null=True, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, blank=True, null=True, on_delete=models.CASCADE)
    miscellaneous = models.ForeignKey(AdditionalInfo, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

