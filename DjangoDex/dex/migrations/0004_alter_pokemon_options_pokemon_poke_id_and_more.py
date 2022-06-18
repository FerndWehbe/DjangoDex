# Generated by Django 4.0.5 on 2022-06-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0003_pokemon_hidden_ability'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={'ordering': ['poke_id']},
        ),
        migrations.AddField(
            model_name='pokemon',
            name='poke_id',
            field=models.IntegerField(blank=True, default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
