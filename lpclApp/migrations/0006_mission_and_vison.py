# Generated by Django 5.0.6 on 2024-05-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lpclApp", "0005_about_us_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mission_and_Vison",
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
                ("mission", models.CharField(max_length=250)),
                ("vision", models.CharField(max_length=250)),
            ],
        ),
    ]
