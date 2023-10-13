from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product1(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/')
    page = models.IntegerField()
    outofstock = models.BooleanField(default=False)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField('Product1', through = 'OrderItem')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} on {self.order_date}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product1', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits = 10, decimal_places = 2)

