# Generated by Django 4.2.5 on 2023-09-26 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "avatar",
                    models.ImageField(default="/default-avatar.png", upload_to=""),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("OTHER", "Other"),
                        ],
                        default="OTHER",
                        max_length=20,
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(default="VN", max_length=2),
                ),
                ("city", models.CharField(default="Ho Chi Minh", max_length=200)),
                (
                    "followers",
                    models.ManyToManyField(
                        related_name="following", to="profiles.profile"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "profile",
            },
        ),
    ]