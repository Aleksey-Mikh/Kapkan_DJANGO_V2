from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserEditForm, UserRegisterForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserEditForm
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone',)}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # fieldsets = (
    #     (None, {
    #         'fields': ('username', 'first_name', 'last_name', 'email', 'phone',)
    #     }),
    # )
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone',)
    search_fields = ('title',)

admin.site.register(CustomUser, CustomUserAdmin)
