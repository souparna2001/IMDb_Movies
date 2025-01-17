# Generated by Django 5.0.1 on 2024-01-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('language', models.CharField(max_length=200)),
                ('runtime', models.PositiveIntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('actors', models.CharField(max_length=200)),
            ],
        ),
    ]
