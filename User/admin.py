from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib import auth
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'updated_at')
    list_display_links = (['text'])
    list_filter = ('user', 'created_at', 'updated_at')
    search_fields = ('user','text')
    list_per_page = 25


admin.site.register(Post, PostAdmin)

