from django.urls import path
from . import views

urlpatterns = [
    path("",views.products_view,name="index_page"),
    path("products/",views.products_view,name="products"),
    path("create_product/",views.create_products_view,name="create_product"),
    path("my_order/",views.orders_view,name="my_order"),
    path("my_cart/",views.cart_view,name="my_cart"),
    path("place_order/",views.place_order_view,name="place_order_page"),
    path("edit_number_of_order/<int:pk>",views.edit_number_of_order,name="edit_number_of_order")
]