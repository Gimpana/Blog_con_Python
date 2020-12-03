# Generated by Django 3.1.3 on 2020-12-03 16:46

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.CharField(max_length=50, verbose_name='Descripción')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creado el ')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categoria',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('public', models.BooleanField(verbose_name='¿Publicado?')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creado el ')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Editado el ')),
                ('categories', models.ManyToManyField(blank=True, related_name='articles', to='blog.Category', verbose_name='Categorias')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
