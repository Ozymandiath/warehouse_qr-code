# Generated by Django 4.1.2 on 2022-10-15 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='link',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
    ]
