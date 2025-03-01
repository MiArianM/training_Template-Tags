from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(POST)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
    list_filter = ('author',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}