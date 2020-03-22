from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    modified_at = models.DateTimeField('Ultima modificação', auto_now=True)

    class Meta:
        abstract = True


class Author(Base):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Biografia')
    image = StdImageField('Imagem', upload_to='authors', variations={
                          'thumb': {'width': 480, 'height': 480, 'crop': True}})
    birth_date = models.DateField('Nascimento', blank=True, null=True)
    death_date = models.DateField('Falecimento', blank=True, null=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ('-created_at', 'name')

    def __str__(self):
        return self.name


class Language(Base):
    name = models.CharField('Língua', max_length=100)

    class Meta:
        verbose_name = 'Língua'
        verbose_name_plural = 'Línguas'
        ordering = ('-created_at', 'name')

    def __str__(self):
        return self.name
