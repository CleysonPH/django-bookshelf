from bookshelf.views import mark_book_has_read, mark_book_has_reading, mark_book_has_want_read
from django.urls import path


app_name = 'bookshelf'
urlpatterns = [
    path('<int:pk>/lido', mark_book_has_read, name='mark-book-has-read'),
    path('<int:pk>/lendo', mark_book_has_reading, name='mark-book-has-reading'),
    path('<int:pk>/quer_ler', mark_book_has_want_read,
         name='mark-book-has-want-read'),
]
