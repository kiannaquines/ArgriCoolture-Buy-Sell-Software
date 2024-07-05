from django.urls import path
from . import views

urlpatterns = [

    # Default Url
    path("",views.login_view, name="login"),
    path("register/",views.register_view, name="register"),
    path("logout/",views.logout_account, name="logout"),
    path("dashboard/",views.dashboard_view, name="dashboard"),
    path("farmer/",views.farmer_view, name="farmer"),
    path("trader/",views.trader_view, name="trader"),
    path("supplier/",views.supplier_view, name="supplier"),
    path("items/",views.items_view, name="items"),
    path("transaction/",views.transaction_view, name="transaction"),
    path("cart/",views.cart_view, name="cart"),
    path("stock_inventory/",views.export_stock_info, name="export_stock_info"),
    
    # Add Url
    path("add_item/",views.add_item_view, name="add_item"),
    path("add_farmer/",views.add_farmer_view, name="add_farmer"),
    path("add_trader/",views.add_trader_view, name="add_trader"),
    path("add_supplier/",views.add_supplier_view, name="add_supplier"),


    # Edit Url
    path("edit_item/<int:pk>",views.edit_item_view, name="edit_item"),
    path("edit_farmer/<int:pk>",views.edit_farmer_view, name="edit_farmer"),
    path("edit_trader/<int:pk>",views.edit_trader_view, name="edit_trader"),
    path("edit_supplier/<int:pk>",views.edit_supplier_view, name="edit_supplier"),

    # Delete Url
    path("delete_item/<int:pk>",views.delete_item_view, name="delete_item"),
    path("delete_farmer/<int:pk>",views.delete_farmer_view, name="delete_farmer"),
    path("delete_trader/<int:pk>",views.delete_trader_view, name="delete_trader"),
    path("delete_supplier/<int:pk>",views.delete_supplier_view, name="delete_supplier"),
    path("delete_transaction/<int:pk>",views.delete_transaction_view, name="delete_transaction"),
    path("delete_cart/<int:pk>",views.delete_cart_view, name="delete_cart"),
]