from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from utiles.generate_code import genrate_code
from products.models import Products



CART_OPTION = (
    ('in_progress','in_progress'),
    ('completed','completed'),
)
 
class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_user' ,on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(_("Status"), max_length=50,choices=CART_OPTION)
    coupon = models.ForeignKey("Coupon",related_name='cart_coupon', verbose_name=_("Coupon"), on_delete=models.SET_NULL,blank=True, null=True)
    total_after_coupon = models.FloatField(_("Total_After_Coupon"),blank=True, null=True)


    def __str__(self): 
        return str(self.user)

    def get_total(self):
        total = 0
        for item in self.cart_detail.all():
            total += item.total
        return round(total,2)

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cart_detail')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL,blank=True, null=True, related_name='product_cart')
    quantity = models.PositiveIntegerField(_("Quntity") ,default=1)
    total = models.PositiveIntegerField(_("Total"),blank=True, null=True)

    def __str__(self):
        return str(self.cart)


ORDER_OPTION = (
    ('recived','recived'),
    ('processed','processed'),
    ('shipped','shipped'),
    ('delevered','delevered'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    code = models.CharField(_("Id"), max_length=10, default=genrate_code)
    status = models.CharField(_("Status"), max_length=50,choices=ORDER_OPTION, default='recived')
    order_time = models.DateTimeField(_("Order_time"),default=timezone.now)
    delevery_time = models.DateField(_("Delevery_time"), blank=True, null=True)
    coupon = models.ForeignKey("Coupon",related_name='order_coupon', verbose_name=_("Coupon"), on_delete=models.SET_NULL,blank=True, null=True)
    total_after_coupon = models.FloatField(_("Total_After_Coupon"),blank=True, null=True)

    def __str__(self):
        return f'{self.code} - {str(self.user)}'
    
    def save(self, *args, **kwargs):
       week = datetime.timedelta(days=7)
       self.delevery_time = self.order_time + week
       super(Order, self).save(*args, **kwargs) 


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='order_detail')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL,blank=True, null=True, related_name='product_order')
    price = models.FloatField(_("Price"))
    quantity = models.PositiveIntegerField(_("Quntity"))
    total = models.PositiveIntegerField(_("Total"),blank=True, null=True)


    def __str__(self):
        return str(self.order)
    

class Coupon(models.Model):
    code = models.CharField(_("Code"), max_length=50)
    discount = models.PositiveIntegerField(_("Discount"))
    quantity = models.PositiveIntegerField(_("Quantity"))
    start_date = models.DateTimeField(_("Start Date"),default=timezone.now)
    end_date = models.DateTimeField(_("End Date"))

    def __str__(self):
        return f"{self.code} - {self.discount}% off"
    
    def save(self, *args, **kwargs):
       week = datetime.timedelta(days=7)
       self.end_date = self.start_date + week
       super(Coupon, self).save(*args, **kwargs) 
