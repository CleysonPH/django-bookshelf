import datetime
from django.test import TestCase

from catalog.models import Language, Genre, Author, Book


class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='Português')

    def setUp(self):
        self.language = Language.objects.get(pk=1)

    def test_language_created_at_label(self):
        field_label = self.language._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'Data de criação')

    def test_language_modified_at_label(self):
        field_label = self.language._meta.get_field('modified_at').verbose_name
        self.assertEqual(field_label, 'Ultima modificação')

    def test_language_name_label(self):
        field_label = self.language._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Língua')

    def test_language_str(self):
        self.assertEqual(str(self.language), self.language.name)


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Ficção')

    def setUp(self):
        self.genre = Genre.objects.get(pk=1)

    def test_genre_created_at_label(self):
        field_label = self.genre._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'Data de criação')

    def test_genre_modified_at_label(self):
        field_label = self.genre._meta.get_field('modified_at').verbose_name
        self.assertEqual(field_label, 'Ultima modificação')

    def test_genre_name_label(self):
        field_label = self.genre._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Gênero')

    def test_genre_str(self):
        self.assertEqual(str(self.genre), self.genre.name)


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            name='J. R. R. Tolkien',
            description='Escritor incrivel',
            birth_date=datetime.date(day=3, month=1, year=1982),
            death_date=datetime.date(day=2, month=9, year=1973),
        )

    def setUp(self):
        self.author = Author.objects.get(pk=1)

    def test_author_created_at_label(self):
        field_label = self.author._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'Data de criação')

    def test_author_modified_at_label(self):
        field_label = self.author._meta.get_field('modified_at').verbose_name
        self.assertEqual(field_label, 'Ultima modificação')

    def test_author_name_label(self):
        field_label = self.author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Nome')

    def test_author_description_label(self):
        field_label = self.author._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'Biografia')

    def test_author_image_label(self):
        field_label = self.author._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'Imagem')

    def test_author_birth_date_label(self):
        field_label = self.author._meta.get_field('birth_date').verbose_name
        self.assertEqual(field_label, 'Nascimento')

    def test_author_death_date_label(self):
        field_label = self.author._meta.get_field('death_date').verbose_name
        self.assertEqual(field_label, 'Falecimento')

    def test_author_str(self):
        self.assertEqual(str(self.author), self.author.name)


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title='O Senhor dos Anéis: A Sociedade do Anel',
            summary='Livro muito bom',
            isbn='9788533613379',
        )

    def setUp(self):
        self.book = Book.objects.get(pk=1)

    def test_book_created_at_label(self):
        field_label = self.book._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'Data de criação')

    def test_book_modified_at_label(self):
        field_label = self.book._meta.get_field('modified_at').verbose_name
        self.assertEqual(field_label, 'Ultima modificação')

    def test_book_title_label(self):
        field_label = self.book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Título')

    def test_book_summary_label(self):
        field_label = self.book._meta.get_field('summary').verbose_name
        self.assertEqual(field_label, 'Resumo')

    def test_book_isbn_label(self):
        field_label = self.book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_book_author_label(self):
        field_label = self.book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'Autor')

    def test_book_genre_label(self):
        field_label = self.book._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'Gênero')

    def test_book_language_label(self):
        field_label = self.book._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'Língua')

    def test_book_image_label(self):
        field_label = self.book._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'Imagem')

    def test_book_str(self):
        self.assertEqual(str(self.book), self.book.title)
