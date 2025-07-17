from django.db import models


# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=100)  
    price=models.DecimalField(default=0,decimal_places=2,max_digits=20)
    description=models.CharField(max_length=500,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/')

    is_sale= models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=15)


    def __str__(self):
        return self.name


