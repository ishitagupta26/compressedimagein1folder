# Generated by Django 5.0.6 on 2024-07-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CompressedImage",
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
                ("compressed_image", models.ImageField(upload_to="compressed_images/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
