from django.shortcuts import render, redirect, get_object_or_404

from .models import BookshelfItem
from catalog.models import Book


def mark_book_has_read(request, pk):
    book = get_object_or_404(Book, pk=pk)
    try:
        bookshelf_item = BookshelfItem.objects.get(
            user=request.user,
            book=book
        )
        bookshelf_item.status = 'read'
        bookshelf_item.save()
    except BookshelfItem.DoesNotExist:
        bookshelf_item = BookshelfItem.objects.create(
            user=request.user,
            book=book,
            status='read'
        )

    return redirect('catalog:book-detail', pk=book.pk)


def mark_book_has_reading(request, pk):
    book = get_object_or_404(Book, pk=pk)
    try:
        bookshelf_item = BookshelfItem.objects.get(
            user=request.user,
            book=book
        )
        bookshelf_item.status = 'reading'
        bookshelf_item.save()
    except BookshelfItem.DoesNotExist:
        bookshelf_item = BookshelfItem.objects.create(
            user=request.user,
            book=book,
            status='reading'
        )

    return redirect('catalog:book-detail', pk=book.pk)


def mark_book_has_want_read(request, pk):
    book = get_object_or_404(Book, pk=pk)
    try:
        bookshelf_item = BookshelfItem.objects.get(
            user=request.user,
            book=book
        )
        bookshelf_item.status = 'want'
        bookshelf_item.save()
    except BookshelfItem.DoesNotExist:
        bookshelf_item = BookshelfItem.objects.create(
            user=request.user,
            book=book,
            status='want'
        )

    return redirect('catalog:book-detail', pk=book.pk)
