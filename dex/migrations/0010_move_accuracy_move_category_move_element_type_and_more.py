# Generated by Django 4.0.5 on 2022-07-27 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0009_alter_move_options_alter_movebylevel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='accuracy',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='category',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='element_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dex.elementtype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='power',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='pp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='probability',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
