from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    USER_TYPE = (
        ('FARMER','FARMER'),
        ('TRADER','TRADER')
    )

    contact_number = models.CharField(max_length=255)
    barangay = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    user_type = models.TextField(choices=USER_TYPE,help_text="Select user type of the user",default=USER_TYPE[0])

    def __str__(self):
        return self.username 
    
    class Meta:
        db_table = "users_tbl"
        verbose_name = "User"
        verbose_name_plural = "Users"

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True,unique=True)
    supplier_name = models.CharField(max_length=255)
    supplier_address = models.CharField(max_length=255)
    supplier_postal_code = models.CharField(max_length=255)
    supplier_barangay = models.CharField(max_length=255)
    supplier_mobile_number = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.supplier_name) 
    
    class Meta:
        db_table = "supplier_tbl"
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

class Item(models.Model):

    STATUS = (
        ('GOOD CONDITION','GOOD CONDITION'),
        (' NOT IN GOOD CONDITION','NOT IN GOOD CONDITION')
    )

    MEASUREMENT = (
        ('Kilogram','Kilogram'),
        ('Grams','Grams'),
        ('Ounces','Ounces'),
    )

    VARIETY = (
        ('Fiji Dwarf','Fiji Dwarf'),
        ('Golden Malay','Golden Malay'),
        ('King Coconut','King Coconut'),
        ('West Coast Tall','West Coast Tall'),
        ('Macapuno','Macapuno'),
        ('Mestiso','Mestiso'),
        ('Matatag','Matatag'),
        ('Masipag','Masipag'),
        ('RC22','RC22'),
        ('Flint Corn','Flint Corn'),
        ('Sweet Corn','Sweet Corn'),
        ('Flour Corn','Flour Corn'),
    )

    ITEM = (
        ('COCONUT','COCONUT'),
        ('PALAY','PALAY'),
        ('CORN','CORN'),
    )

    item_id = models.AutoField(primary_key=True,unique=True)
    item_name = models.CharField(max_length=255,choices=ITEM,null=True)
    item_variety = models.CharField(max_length=255,choices=VARIETY,null=True)
    item_desc = models.TextField(max_length=500)
    item_status = models.TextField(choices=STATUS,default=STATUS[0])
    item_image = models.ImageField(upload_to="img/item_img",null=True)
    item_supplier = models.ForeignKey(Supplier,on_delete=models.DO_NOTHING,default="Select Supplier",null=True)
    item_quantity = models.IntegerField()
    item_price = models.IntegerField(help_text="Item price per kilo",null=True)
    item_date_added = models.DateField(auto_now_add=True)
    item_measurement = models.CharField(max_length=255,choices=MEASUREMENT,default=MEASUREMENT[0],null=True)
    item_kilo_per_measurement = models.CharField(max_length=255,default="",null=True)


    def __str__(self) -> str:
        return self.item_name
    
    class Meta:
        db_table = "item_tbl"
        verbose_name = "Item"
        verbose_name_plural = "Items"

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True,unique=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    order_quantity = models.IntegerField(null=True, default=1)
    is_checkedOut = models.BooleanField(default=False)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.item_name}"
    

    class Meta:
        db_table = "cart_tbl"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255,unique=True,db_index=True,null=True)
    order_product = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    user_transaction = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    amount_per_product = models.IntegerField(null=True)
    quantity_per_product = models.IntegerField(null=True)
    date_transaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id}"

    class Meta:
        db_table = "transaction_tbl"
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"