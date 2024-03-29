# Generated by Django 4.0.4 on 2022-04-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_note_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='num_visits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='calories',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='carbs',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='cho',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='fat',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='pro',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='sod',
            field=models.CharField(default='', max_length=10),
        ),
    ]
