from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#Customer Model
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    profile_pic = models.ImageField(default='avatar.png',null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name



#Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name



# Product Model
class Product(models.Model):
    CATEGORY = [
            ('Indoor','Indoor'),
            ('Outdoor','Outdoor')
            ]

    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name




#Order Model
class Order(models.Model):
    STATUS = [
            ('Confirmation Pending','Confirmation Pending'),
            ('Confirmed','Confirmed'),
            ('Shipped','Shipped'),
            ('In Transit','In Transit'),
            ('Out For Delivery','Out For Delivery'),
            ('Delivered','Delivered')
            ]

    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS,default='Confirmation Pending')

    def __str__(self):
        return self.customer.name
