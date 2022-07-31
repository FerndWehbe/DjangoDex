# Generated by Django 4.0.5 on 2022-07-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0008_rename_moves_move_rename_movesbylevel_movebylevel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='move',
            options={'ordering': ['move_name']},
        ),
        migrations.AlterModelOptions(
            name='movebylevel',
            options={'ordering': ['learned_level']},
        ),
        migrations.AddField(
            model_name='move',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]