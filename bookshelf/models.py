from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    modified_at = models.DateTimeField('Ultima modificação', auto_now=True)

    class Meta:
        abstract = True


class BookshelfItem(Base):

    STATUS_CHOICE = (
        ('reading', 'Estou lendo'),
        ('read', 'Já li'),
        ('want', 'Quero ler'),
        ('stop', 'Abandonei'),
    )

    user = models.ForeignKey(
        'auth.User', verbose_name='Usuário', on_delete=models.CASCADE)
    book = models.ForeignKey(
        'catalog.Book', verbose_name='Livro', on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=7, choices=STATUS_CHOICE)

    class Meta:
        verbose_name = 'Item da prateleira'
        verbose_name_plural = 'Itens da prateleira'

    def __str__(self):
        return f'{self.status} {self.book.title}'
