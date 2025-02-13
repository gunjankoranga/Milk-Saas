from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone_number', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'phone_number', 'email')
    ordering = ('username',)
    
    fieldsets = (
        (None, {'fields': ('username', 'phone_number', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
