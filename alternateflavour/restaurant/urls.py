from django.urls import path
from .import views

urlpatterns = [
    path('', views.restaurant, name="restaurant"),
    #     path('<int:id>', views.productView, name="productView"),
    #     path('cart/', views.cart, name="cart"),
    #     path('checkout/', views.checkout, name="checkout"),
    #     path('update_item/', views.updateItem, name="update_item"),
    #     path('process_order/', views.processOrder, name="process_order"),
]