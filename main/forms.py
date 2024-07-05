from django import forms
from .models import CustomUser,Supplier,Item,Transaction
from django.contrib.auth.hashers import make_password

class SupplierForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(SupplierForm,self).__init__(*args,**kwargs)
        self.fields['supplier_name'].label = "Supplier name"
        self.fields['supplier_address'].label = "Address"
        self.fields['supplier_postal_code'].label = "Postal code"
        self.fields['supplier_barangay'].label = "Barangay"
        self.fields['supplier_mobile_number'].label = "Mobile Number"

    class Meta:
        model = Supplier
        fields = ["supplier_name","supplier_address","supplier_postal_code","supplier_barangay","supplier_mobile_number"]

        widgets = {
            'supplier_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Supplier Name'}),
            'supplier_address': forms.Textarea(attrs={'class':'form-control form-control-lg','rows':'5','placeholder':'Address'}),
            'supplier_postal_code': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Postal Code'}),
            'supplier_barangay': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Barangay'}),
            'supplier_mobile_number': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Mobile Number'}),
        }



class ItemForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ItemForm,self).__init__(*args,**kwargs)
        self.fields['item_name'].label = "Item Name"
        self.fields['item_desc'].label = "Item Description"
        self.fields['item_variety'].label = "Item Variety"
        self.fields['item_status'].label = "Item Status"
        self.fields['item_quantity'].label = "Item Quantity"        
        self.fields['item_measurement'].label = "Item Measurement"        
        self.fields['item_kilo_per_measurement'].label = "Item Weight"    
        self.fields['item_supplier'].label = "Item Supplier"
        self.fields['item_image'].label = "Item Image"    
        self.fields['item_price'].label = "Item Price"    

    class Meta:
        model = Item
        fields = ["item_name","item_variety","item_desc","item_price","item_image","item_supplier","item_desc","item_status","item_quantity","item_measurement","item_kilo_per_measurement",]
        widgets = {
            'item_name': forms.Select(attrs={'class':'form-select'}),
            'item_desc': forms.Textarea(attrs={'class':'form-control form-control-lg','rows':'5','placeholder':'Item Description'}),
            'item_status': forms.Select(attrs={'class':'form-select'}),
            'item_supplier': forms.Select(attrs={'class':'form-select'}),
            'item_variety': forms.Select(attrs={'class':'form-select'}),
            'item_image': forms.FileInput(attrs={'class':'form-control'}),
            'item_price': forms.TextInput(attrs={'class':'form-control'}),
            'item_measurement': forms.Select(attrs={'class':'form-select'}),
            'item_quantity': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Item Quantity'}),
            'item_kilo_per_measurement': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Item Kilograms/Weight'}),
        }


class RegisterForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields["first_name"].label = "Firstname"
        self.fields["last_name"].label = "Lastname"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm Password"
        self.fields["email"].label = "Email Address"
        self.fields["postal_code"].label = "Postal Code"
        self.fields["user_type"].label = "User Type"
        self.fields["contact_number"].label = "Contact Number"
        self.fields["barangay"].label = "Barangay"
        self.fields["address"].label = "Address"
    
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Username'}),help_text="Enter your username for your account.")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Confirm Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Lastname'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Email Address'}))
    user_type = forms.CharField(widget=forms.Select(attrs={'class':'form-select form-select-lg',},choices=(('FARMER','FARMER'),('TRADER','TRADER'))))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Postal Code'}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Contact Number'}))
    barangay = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Barangay'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg','placeholder':'Address','rows':'3'}))
    


class TraderForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(TraderForm,self).__init__(*args,**kwargs)
        self.fields['user_type'].label = "Select User type"
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["password"].required = True
    
    class Meta:
        model = CustomUser
        fields = ["username","first_name","last_name","password","user_type","contact_number","barangay","postal_code","address",]

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Firstname'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Lastname'}),
            'password': forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Password'}),
            'user_type': forms.Select(attrs={'class':'form-select'}),
            'contact_number': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Contact Number'}),
            'barangay': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Barangay'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Postal Code'}),
            'address': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Address'}),
        }


class UpdateTraderForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UpdateTraderForm,self).__init__(*args,**kwargs)
        self.fields['user_type'].label = "Select User type"
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
    
    class Meta:
        model = CustomUser
        fields = ["username","first_name","last_name","user_type","contact_number","barangay","postal_code","address",]

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Firstname'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Lastname'}),
            'user_type': forms.Select(attrs={'class':'form-select'}),
            'contact_number': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Contact Number'}),
            'barangay': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Barangay'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Postal Code'}),
            'address': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Address'}),
        }


        exclude = ("password",)

class FarmerForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super(FarmerForm,self).__init__(*args,**kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    class Meta:
        model = CustomUser
        fields = ["username","first_name","last_name","password","user_type","contact_number","barangay","postal_code","address",]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Firstname'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Lastname'}),
            'password': forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Password'}),
            'user_type': forms.Select(attrs={'class':'form-select'}),
            'contact_number': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Contact Number'}),
            'barangay': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Barangay'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Postal Code'}),
            'address': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Address'}),
        }


class UpdateFarmerForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super(UpdateFarmerForm,self).__init__(*args,**kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    class Meta:
        model = CustomUser
        fields = ["username","first_name","last_name","user_type","contact_number","barangay","postal_code","address",]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Firstname'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Lastname'}),
            'user_type': forms.Select(attrs={'class':'form-select'}),
            'contact_number': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Contact Number'}),
            'barangay': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Barangay'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Postal Code'}),
            'address': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Address'}),
        }

        exclude = ("password",)


# class OrderForm(forms.ModelForm):
    
#     class Meta:
#         model = Order
#         fields = ["order_by","product","order_quantity",]
#         widgets = {
#             'order_by': forms.Select(attrs={'class':'form-select'}),
#             'product': forms.Select(attrs={'class':'form-select'}),
#             'order_quantity': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Order Quantity'}),
#         }