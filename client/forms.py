from django import forms
from main.models import Item,Cart

class SellForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(SellForm,self).__init__(*args,**kwargs)
        self.fields['item_name'].label = "Product Name"
        self.fields['item_desc'].label = "Product Description"
        self.fields['item_status'].label = "Product Status"
        self.fields['item_quantity'].label = "Product Quantity"        

    class Meta:
        model = Item
        fields = ["item_name","item_desc","item_status","item_quantity","item_supplier","item_image","item_price","item_measurement","item_quantity","item_kilo_per_measurement",]
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Item Name'}),
            'item_desc': forms.Textarea(attrs={'class':'form-control form-control-lg','rows':'5','placeholder':'Item Description'}),
            'item_status': forms.Select(attrs={'class':'form-select'}),
            'item_supplier': forms.Select(attrs={'class':'form-select'}),
            'item_image': forms.FileInput(attrs={'class':'form-control'}),
            'item_price': forms.TextInput(attrs={'class':'form-control'}),
            'item_measurement': forms.Select(attrs={'class':'form-select'}),
            'item_quantity': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Item Quantity'}),
            'item_kilo_per_measurement': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Item Kilograms/Weight'}),
        }


class UpdateOrderQuantityForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UpdateOrderQuantityForm,self).__init__(*args,**kwargs)
        self.fields['order_quantity'].widget.attrs.update({'class':'form-control form-control-lg','placeholder':'Enter Order Quantity'})

    class Meta:
        model = Cart
        fields = ("order_quantity",)


        
