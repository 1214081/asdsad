# Generated by Django 4.1.5 on 2023-01-15 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Preprocessing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.TimeField()),
                ("tweets", models.CharField(max_length=255)),
                ("clear", models.CharField(max_length=255)),
                ("token_tweets", models.CharField(max_length=255)),
                ("freq_words", models.CharField(max_length=255)),
                ("stemmed_words", models.CharField(max_length=255)),
                ("polarity_score", models.IntegerField()),
                ("polarity", models.CharField(max_length=255)),
                ("score", models.IntegerField()),
            ],
        ),
    ]