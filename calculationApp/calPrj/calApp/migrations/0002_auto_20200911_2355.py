# Generated by Django 3.1.1 on 2020-09-11 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='fbad',
            new_name='fbed',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='fbat',
            new_name='fbet',
        ),
    ]