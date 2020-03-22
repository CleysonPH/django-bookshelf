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
