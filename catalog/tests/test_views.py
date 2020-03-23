from django.test import TestCase
from django.urls import reverse

from catalog.models import Language, Genre, Author, Book


class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name='G. R. R. Martin')
        language = Language.objects.create(name='Português')
        genre_ficcao = Genre.objects.create(name='Ficção')
        genre_fantasia = Genre.objects.create(name='Fantasia')

        for index in range(1, 11):
            book = Book.objects.create(
                title=f'As Crônicas de Gelo e Fogo - Livro {index}',
                summary='Sumario do livro',
                isbn='9780553386790',
                author=author,
                language=language,
            )
            book.genre.add(genre_fantasia)
            book.genre.add(genre_ficcao)
            book.save()

    def setUp(self):
        self.books = Book.objects.all()

    def test_view_url_exists_at_desire_location(self):
        response = self.client.get('/catalogo/livros')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('catalog:books-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('catalog:books-list'))
        self.assertTemplateUsed(response, 'catalog/book_list.html')

    def test_view_list_all_books(self):
        response = self.client.get(reverse('catalog:books-list'))
        self.assertTrue('book_list' in response.context)
        self.assertTrue(len(response.context['book_list']) == 10)
