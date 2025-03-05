from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(POST)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
    list_filter = ('author',)
    search_fields = ('title',)
    reading_time = ('reading_time',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'created')
    search_fields = ('title',)
