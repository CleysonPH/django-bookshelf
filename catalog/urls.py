from django.urls import path

from .views import BooksListView


app_name = 'catalog'
urlpatterns = [
    path('livros', BooksListView.as_view(), name='books-list'),
]
