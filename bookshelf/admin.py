from django.contrib import admin

from .models import Language, Genre, Author, Book


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at')


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at')
