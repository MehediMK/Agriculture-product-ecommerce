from django.contrib import admin
from .models import User_info

# Register your models here.

@admin.register(User_info)
class AccountAdmin(admin.ModelAdmin):

    list_display = ['pk', 'user', 'gender', 'address', 'phone']
    list_display_links = ['user']