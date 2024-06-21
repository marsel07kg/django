# Generated by Django 5.0.6 on 2024-06-20 18:30

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('user_email', models.EmailField(default='@gmail.com', max_length=254, verbose_name='Ваша почта')),
                ('image_book', models.ImageField(upload_to='images/', verbose_name='Загрузите фото')),
                ('about_book', models.TextField(verbose_name='о этом книге')),
                ('genre', models.CharField(choices=[('action movie', 'action movie'), ('romance', 'romance'), ('Fantastic', 'Fantastic'), ('Mystic', 'Mystic'), ('learn', 'learn')], max_length=100, verbose_name='Жанр книги')),
                ('date_of_create', models.DateField(verbose_name='Дата создание')),
                ('urls_for_B', models.URLField(verbose_name='Ссылка на книгу')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата опубликования')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rewiews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reviews_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_book', to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(default=100, null=True)),
                ('tags', models.ManyToManyField(null=True, to='books.tag')),
            ],
        ),
    ]
