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


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['page_title'] = 'Detalhes'
        context['page_description'] = 'Todas as informações do livro'
        return context


class AuthorListView(ListView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Autores'
        context['page_description'] = 'Lista com todos os autores cadatrados na plataforma'
        return context


class AuthorDetailView(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['page_title'] = 'Detalhes'
        context['page_description'] = 'Todas as informações do autor'
        return context


class GenreListView(ListView):
    model = Genre

    def get_context_data(self, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Gêneros'
        context['page_description'] = 'Lista com todos os gêneros cadatrados na plataforma'
        return context
