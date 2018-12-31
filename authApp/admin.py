from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['name','email','password','contact_no']

admin.site.register(CustomUser, CustomUserAdmin);
# Register your models here.
