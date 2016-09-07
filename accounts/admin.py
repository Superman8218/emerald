from django.contrib import admin

from .models import UserProfile, Account

# Register your models here.

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    pass

@admin.register(Account)
class Account(admin.ModelAdmin):
    pass
