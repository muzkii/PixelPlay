from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50)
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return self.name
    
    @property
    def is_high_rating(self):
        return self.rating >= 4.5