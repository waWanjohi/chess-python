# Generated by Django 4.0.6 on 2022-07-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0004_alter_game_game_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="capture",
            name="color",
            field=models.CharField(max_length=10),
        ),
    ]
