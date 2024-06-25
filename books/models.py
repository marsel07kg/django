from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    GENRE = (
        ('action movie', 'action movie'),
        ('romance', 'romance'),
        ('Fantastic', 'Fantastic'),
        ('Mystic', 'Mystic'),
        ('learn', 'learn'),
    )
    name = models.CharField(max_length=100, verbose_name="Название книги")
    user_email = models.EmailField(default='@gmail.com', verbose_name="Ваша почта")
    image_book = models.ImageField(upload_to='images/', verbose_name='Загрузите фото')
    about_book = models.TextField(verbose_name="о этом книге")
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name="Жанр книги")
    date_of_create = models.DateField(verbose_name="Дата создание")
    urls_for_B = models.URLField(max_length=200, verbose_name="Ссылка на книгу")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата опубликования")

    def __str__(self):
        return f'{self.name}-{self.genre}'

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


# Create your models here.


class Rewiews(models.Model):
    reviews_book = models.ForeignKey(Book, on_delete=models.CASCADE,
                                     related_name='reviews_book')
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f'{self.stars}-{self.reviews_book}'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Library(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=100, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

# Create your models here.
