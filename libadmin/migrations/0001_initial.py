# Generated by Django 2.1 on 2019-05-04 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('issue', models.CharField(default='N', max_length=1)),
                ('idate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Luser',
            fields=[
                ('uid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libadmin.Dept')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='libadmin.Luser'),
        ),
    ]