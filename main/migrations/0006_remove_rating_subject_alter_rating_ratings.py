# Generated by Django 4.0.3 on 2022-04-01 02:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='subject',
        ),
        migrations.AlterField(
            model_name='rating',
            name='ratings',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]