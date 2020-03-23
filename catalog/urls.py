from django.urls import path

from .views import AuthorListView, BookDetailView, BooksListView


app_name = 'catalog'
urlpatterns = [
    path('livros', BooksListView.as_view(), name='books-list'),
    path('livro/<int:pk>/detalhes', BookDetailView.as_view(), name='book-detail'),
    path('autores', AuthorListView.as_view(), name='authors-list'),
]
