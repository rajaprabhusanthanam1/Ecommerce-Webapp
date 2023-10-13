from django.contrib import admin

# Register your models here.
from .models import Product1,Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_amount')
    list_filter = ('order_date',)
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=('title','price','image','outofstock','page')
    list_filter = ('outofstock','page',)
#ProductAdmin class
admin.site.register(Product1,ProductAdmin)
#class User_Profile(admin.)

