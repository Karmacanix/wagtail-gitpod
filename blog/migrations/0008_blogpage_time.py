# Generated by Django 4.2.16 on 2024-09-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogtagindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='time',
            field=models.TimeField(default='6:02', verbose_name='time in pooland'),
            preserve_default=False,
        ),
    ]
