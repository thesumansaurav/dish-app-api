"""
Customized Admin.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUSerAdmin
from core import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUSerAdmin):
    """Define customized admin class"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_superuser',
                    'is_staff'
                )
            }
        ),
        (
            _('Important dates'), {'fields': ('last_login',)}
        )
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_superuser',
                'is_staff',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
