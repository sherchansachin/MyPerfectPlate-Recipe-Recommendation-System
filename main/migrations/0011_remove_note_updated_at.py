# Generated by Django 4.0.4 on 2022-04-23 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_note_delete_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='updated_at',
        ),
    ]
