"""
Store models
"""

from django.db import models


class Candy(models.Model):
    """Candy model"""

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, default="")

    class Meta:
        verbose_name_plural = "candies"
        ordering = ["name"]

    def __str__(self):
        return self.name
