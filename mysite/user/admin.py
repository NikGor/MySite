from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from mysite.user.models import User

from scripts.utils import translate_model


class UserAdmin(BaseUserAdmin):
    actions = [translate_model]

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'birth_date', 'job_title', 'location', 'is_relocatable', 'linkedin',
            'phone_number',
            'website', 'about_me', 'job_title_de', 'about_me_de')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'birth_date')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


# Перерегистрируем модель User с новым UserAdmin
admin.site.register(User, UserAdmin)
