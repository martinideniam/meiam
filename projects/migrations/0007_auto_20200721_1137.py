# Generated by Django 3.0.4 on 2020-07-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200721_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectspost',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='projects/static/projects/projects'),
        ),
    ]