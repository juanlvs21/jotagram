"""User admin class."""
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from apps.users.models import Profile

@admin.register(Profile) # El decorador funciona para registrar nuestra clase
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk','user','phone_number', 'website')
    list_display_links = ('pk','user')
    # list_editable = ('phone_number', 'website')
    search_fields = ('user__username','user__email', 'user__first_name', 'user__last_name')
    list_filter = ('user__is_active','created', 'modified')

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            ),
        }),
        ('Extra info', {
            'fields': (
                ('phone_number','website'),
                'biography',
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created','modified'),
            ),
        }),
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""
    # Esta clase es para unir Usuario y Perfil
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    # Instancia una nueva clase que herede de usuario
    inlines = (ProfileInline,)

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_superuser'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin) # Registra el modelo que vamos a usar y la clase