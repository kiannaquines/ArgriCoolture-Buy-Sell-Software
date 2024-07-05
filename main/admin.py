from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as OriginalAdmin

class UserCustomAdmin(OriginalAdmin):
    exclude = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'contact_number','barangay','postal_code','address','user_type')}),
        ('Important dates', {'fields': ('last_login',)})
    )
    list_display = ('username','first_name','last_name','date_joined','is_active',)
    list_filter  = ['is_active']


admin.site.register(CustomUser,UserCustomAdmin)
admin.site.register(Cart)
admin.site.register(Transaction)
admin.site.register(Supplier)
admin.site.register(Item)
