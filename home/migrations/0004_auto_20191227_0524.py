# Generated by Django 3.0 on 2019-12-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(path='home/static/img/'),
        ),
    ]
