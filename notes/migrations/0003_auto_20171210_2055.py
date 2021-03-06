# Generated by Django 2.0 on 2017-12-10 20:55

from __future__ import unicode_literals
from django.db import migrations


def create_initial_notes(apps, schema_editor):
    Note = apps.get_model('notes', 'Note')

    Note(name='Whisky 1', description='Geranium', rating=8).save()
    Note(name='Whisky 2', description='Olio balsamico di Modena', rating=10).save()
    Note(name='Whisky 3', description='Peach', rating=8.50).save()


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20171210_2018'),
    ]

    operations = [
        migrations.RunPython(create_initial_notes),
    ]
