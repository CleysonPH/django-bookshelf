from django.contrib import admin

from .models import BookshelfItem


@admin.register(BookshelfItem)
class BookshelfItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'created_at', 'modified_at')
