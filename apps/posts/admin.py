"""Post admin class."""
# Django
from django.contrib import admin

# Models
from apps.posts.models import Post

@admin.register(Post) # El decorador funciona para registrar nuestra clase
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('pk','user', 'title', 'photo')
    list_display_links = ('pk','user')
    search_fields = ('user__username','user__email', 'user__first_name', 'user__last_name', 'title', 'photo')
    list_filter = ('created', 'modified')

    readonly_fields = ('created', 'modified')