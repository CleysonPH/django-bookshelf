from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Base(models.Model):
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    modified_at = models.DateTimeField('Ultima modificação', auto_now=True)

    class Meta:
        abstract = True


class Review(Base):
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Crítica')
    rating = models.IntegerField('Nota', validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    book = models.ForeignKey(
        'catalog.Book',
        verbose_name='Livro',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'auth.User',
        verbose_name="Usuário",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'{self.book.title} - {self.title} - {self.rating}'
