# Generated by Django 5.0.6 on 2024-06-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="genre",
        ),
        migrations.AddField(
            model_name="customuser",
            name="types_book",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
