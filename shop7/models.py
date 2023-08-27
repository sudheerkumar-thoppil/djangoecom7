from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=50)
    category =models.ForeignKey('Category',on_delete=models.CASCADE)
    productprice =models.FloatField()
    productimage= models.ImageField(upload_to='media')

    def __str__(self):
        return self.productname

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category