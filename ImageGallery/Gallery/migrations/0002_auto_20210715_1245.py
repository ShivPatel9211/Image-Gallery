# Generated by Django 3.2.5 on 2021-07-15 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
    ]
