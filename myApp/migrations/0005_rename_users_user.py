# Generated by Django 4.1.4 on 2022-12-15 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_remove_users_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]