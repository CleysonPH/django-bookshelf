from django.db import models
from stdimage import StdImageField
from django.urls import reverse


class Base(models.Model):
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    modified_at = models.DateTimeField('Ultima modificação', auto_now=True)

    class Meta:
        abstract = True


class Author(Base):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Biografia')
    image = StdImageField('Imagem', upload_to='authors', variations={
                          'thumb': {'width': 64, 'height': 64, 'crop': True}})
    birth_date = models.DateField('Nascimento', blank=True, null=True)
    death_date = models.DateField('Falecimento', blank=True, null=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ('-created_at', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:author-detail', kwargs={'pk': self.pk})


class Language(Base):
    name = models.CharField('Língua', max_length=100)

    class Meta:
        verbose_name = 'Língua'
        verbose_name_plural = 'Línguas'
        ordering = ('-created_at', 'name')

    def __str__(self):
        return self.name


class Genre(Base):
    name = models.CharField('Gênero', max_length=200)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ('-created_at', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:genre-detail', kwargs={'pk': self.pk})


class Book(Base):
    title = models.CharField('Título', max_length=200)
    summary = models.TextField('Resumo')
    isbn = models.CharField('ISBN', max_length=13)
    image = StdImageField('Imagem', upload_to='books', variations={
                          'thumb': {'width': 64, 'height': 92, 'crop': True}})
    author = models.ForeignKey(
        "catalog.Author", verbose_name='Autor', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField("catalog.Genre", verbose_name='Gênero')
    language = models.ForeignKey(
        "catalog.Language", verbose_name='Língua', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book-detail', kwargs={'pk': self.pk})

    def get_reading_cout(self):
        return self.bookshelfitem_set.filter(status='reading').count()

    def get_read_cout(self):
        return self.bookshelfitem_set.filter(status='read').count()

    def get_want_read_cout(self):
        return self.bookshelfitem_set.filter(status='want').count()
