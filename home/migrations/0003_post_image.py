# Generated by Django 3.0 on 2019-12-24 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191223_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FilePathField(default=django.utils.timezone.now, path='/img'),
            preserve_default=False,
        ),
    ]
