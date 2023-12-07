from django.urls import path
from .views import OrderList,checkout,add_to_cart,remove_from_cart
from .api import CartListDetailAPI,OrderListAPI,OrderDetailAPI,CreateOrderAPI,ApplyCouponAPI


app_name = 'orders'

urlpatterns =[
    path('', OrderList.as_view(), name='order_list'),
    path('checkout', checkout, name='checkout'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('<int:id>/remove_from_cart', remove_from_cart, name='remove_from_cart'),


    #__api__
    path('api/<str:username>',CartListDetailAPI.as_view()),
    path('api/<str:username>/list',OrderListAPI.as_view()),
    path('api/<str:username>/<int:pk>', OrderDetailAPI.as_view()),

    path('api/<str:username>/create-order',CreateOrderAPI.as_view()),
    path('api/<str:username>/apply-coupon',ApplyCouponAPI.as_view()),




]