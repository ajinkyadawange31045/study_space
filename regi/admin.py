from django.contrib import admin
from .models import Profile

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('username', 'name', 'email', 'phone_number', 'branch', 'semester')
#     search_fields = ('username', 'name', 'email')

# admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile)
