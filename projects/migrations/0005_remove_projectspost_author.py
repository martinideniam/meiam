# Generated by Django 3.0.4 on 2020-07-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projectspost_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectspost',
            name='author',
        ),
    ]
