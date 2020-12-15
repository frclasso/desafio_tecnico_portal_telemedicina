from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core.models import User, Palestrante


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )


admin.site.register(User, UserAdmin)


class PalestranteAdmin(admin.ModelAdmin):

    list_display = [
        'nome',
        'bio'
    ]


admin.site.register(Palestrante, PalestranteAdmin)
