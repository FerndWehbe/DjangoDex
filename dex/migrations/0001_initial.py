# Generated by Django 4.0.5 on 2022-06-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('xp', models.IntegerField()),
                ('image_url', models.URLField()),
                ('poke_url', models.URLField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('special_attack', models.IntegerField()),
                ('special_defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('abilities', models.ManyToManyField(to='dex.ability')),
                ('types', models.ManyToManyField(to='dex.elementtype')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
