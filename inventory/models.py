# inventory/models.py
from django.db import models

class Inventory(models.Model):
    timestamp = models.DateTimeField()
    description = models.TextField()
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    product_type = models.CharField(max_length=50)
    custom_label_0 = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return self.title  # Display the title in the admin interface or shell
