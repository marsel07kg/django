from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
LITERARY_CLUB_CHOICES = (
    ('not_readers', 'Not readers'),
    ('beginners', 'beginners'),
    ('amateur', 'amateur'),
    ('veteran', 'veteran')
)


class CustomRegistrationsForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    status_of_reader = forms.ChoiceField(choices=LITERARY_CLUB_CHOICES, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'age',
            'types_book',
            'status_of_reader',
        )

    def save(self, commit=True):
        user = super(CustomRegistrationsForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

@receiver(post_save, sender=models.CustomUser)
def set_club(sender, instance, created, **kwargs):
    if created:
        status_of_reader = instance.status_of_reader
        if status_of_reader == 'not_readers':
            instance.literary_club = 'not_readers'
        elif status_of_reader == 'beginner':
            instance.literary_club = 'beginner'
        elif status_of_reader == 'amateur':
            instance.literary_club = 'amateur'
        elif status_of_reader == 'veteran':
            instance.literary_club = 'veteran'
        else:
            instance.literary_club = 'Клуб не определен'
        instance.save()
