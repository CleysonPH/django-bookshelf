from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Author, Genre, Book


class BooksListView(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BooksListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Livros'
        context['page_description'] = 'Lista com todos os livros cadatrados na plataforma'
        return context
