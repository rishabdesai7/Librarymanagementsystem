# Generated by Django 2.1 on 2019-05-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libadmin', '0003_auto_20190506_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rcount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]