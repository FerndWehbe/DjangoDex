# Generated by Django 4.0.5 on 2022-06-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0004_alter_pokemon_options_pokemon_poke_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
