# Generated by Django 4.0.2 on 2022-02-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='title',
            field=models.TextField(max_length=150, unique=True),
        ),
    ]