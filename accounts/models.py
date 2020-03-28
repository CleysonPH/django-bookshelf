from django.db import models
from stdimage import StdImageField
from django.urls import reverse


class Base(models.Model):
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    modified_at = models.DateTimeField('Ultima modificação', auto_now=True)

    class Meta:
        abstract = True


class UserProfile(Base):
    image = StdImageField('Imagem de perfil', upload_to='users', default='default.png', variations={
                          'thumb': {'width': 64, 'height': 64, 'crop': True}})
    description = models.TextField('Biografia', blank=True, null=False)
    favorite_genre = models.ForeignKey(
        "catalog.Genre", verbose_name='Gênero favorito', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(
        "auth.User", verbose_name='Usuário', on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Pefil do usuário'
        verbose_name_plural = 'Perfis de usuários'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:user-detail', kwargs={'username': self.user.username})
