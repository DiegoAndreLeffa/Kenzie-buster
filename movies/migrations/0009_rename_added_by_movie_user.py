# Generated by Django 4.2 on 2023-04-12 13:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0008_rename_user_movie_added_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="added_by",
            new_name="user",
        ),
    ]
