from django.contrib import admin

from .models import Language, Genre, Author, Book


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at')


@admin.register(Genre)
class GenreModel(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at')


@admin.register(Author)
class AuthorModel(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'death_date',
                    'created_at', 'modified_at')
