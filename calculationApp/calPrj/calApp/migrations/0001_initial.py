# Generated by Django 3.1.1 on 2020-09-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pod', models.CharField(max_length=20)),
                ('pwt', models.CharField(max_length=20)),
                ('pd', models.CharField(max_length=20)),
                ('ca', models.CharField(max_length=20)),
                ('fbat', models.CharField(max_length=20)),
                ('fbad', models.CharField(max_length=20)),
                ('ad', models.CharField(max_length=20)),
                ('wd', models.CharField(max_length=20)),
                ('swd', models.CharField(max_length=20)),
            ],
        ),
    ]