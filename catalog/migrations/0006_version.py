# Generated by Django 5.0.6 on 2024-08-07 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_created_at_alter_product_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                ("version", models.FloatField(max_length=10, verbose_name="Версия")),
                (
                    "name_version",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Название версии",
                    ),
                ),
                (
                    "sign_version",
                    models.BooleanField(default=True, verbose_name="Активна"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]
