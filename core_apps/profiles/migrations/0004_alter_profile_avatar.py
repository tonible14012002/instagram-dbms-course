# Generated by Django 4.2.5 on 2023-09-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0003_alter_profile__nickname_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.URLField(default="", max_length=2000),
        ),
    ]