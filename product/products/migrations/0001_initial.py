# Generated by Django 5.0.6 on 2024-07-16 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("established_year", models.CharField(max_length=4)),
                ("ceo", models.CharField(max_length=100)),
                ("employees", models.CharField(max_length=50)),
                ("business_nature", models.CharField(max_length=100)),
                ("additional_business", models.CharField(max_length=100)),
                ("turnover", models.CharField(max_length=50)),
                ("banker", models.CharField(max_length=100)),
                ("legal_status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("product_type", models.CharField(max_length=255)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Electric Wire Rope Hoist", "Electric Wire Rope Hoist"),
                            ("Electric Chain Hoist", "Electric Chain Hoist"),
                            ("EOT Crane", "EOT Crane"),
                            ("EOT Crane Accessory", "EOT Crane Accessory"),
                            ("Conveyor", "Conveyor"),
                        ],
                        max_length=50,
                    ),
                ),
                ("speed", models.CharField(blank=True, max_length=50, null=True)),
                ("voltage", models.CharField(blank=True, max_length=50, null=True)),
                ("capacity", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "material_grade",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("frequency", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "automation_grade",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("image", models.ImageField(upload_to="products/")),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=255)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("email", models.EmailField(max_length=254)),
                ("contact_number", models.CharField(max_length=20)),
                ("message", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="inquiries",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]