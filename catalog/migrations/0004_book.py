# Generated by Django 3.0.4 on 2020-03-22 19:50

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Data de criação')),
                ('modified_at', models.DateTimeField(
                    auto_now=True, verbose_name='Ultima modificação')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('summary', models.TextField(verbose_name='Resumo')),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
                ('image', stdimage.models.StdImageField(
                    upload_to='books', verbose_name='Imagem')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                             to='catalog.Author', verbose_name='Autor')),
                ('genre', models.ManyToManyField(
                    to='catalog.Genre', verbose_name='Gênero')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               to='catalog.Language', verbose_name='Língua')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
                'ordering': ('-created_at', 'title'),
            },
        ),
    ]
