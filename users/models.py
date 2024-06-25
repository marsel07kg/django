from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)
LITERARY_CLUB_CHOICES = (
    ("beginner", "beginner"),
    ("not_readers", "not_readers"),
    ("amateur", "amateur"),
    ("veteran", "veteran"),
)


class CustomUser(User):
    phone_number = models.CharField(max_length=14, default="+996")
    age = models.IntegerField(default=18)
    gender = models.TextField(max_length=100, choices=GENDER_CHOICES)
    status_of_reader = models.TextField(max_length=100, choices=LITERARY_CLUB_CHOICES)
    types_book = models.CharField(
        max_length=100, null=True, verbose_name="предпочитаемые книги"
    )

    literary_club = models.CharField(max_length=100, default="Клуб не определен")


@receiver(post_save, sender=CustomUser)
def club(sender, instance, created, **kwargs):
    if created:
        print("Сигнал успешен пользователь зарегистрировалься")
        status_of_reader = instance.status_of_reader
        if status_of_reader == "not_readers":
            instance.literary_club = "not_readers"
        elif status_of_reader == "beginners":
            instance.literary_club = "beginners"
        elif status_of_reader == "amateur":
            instance.literary_club = "amateur"
        elif status_of_reader == "veteran":
            instance.literary_club = "veteran"
        else:
            instance.literary_club = "Клуб не определен"
        instance.save()


# Create your models here.
