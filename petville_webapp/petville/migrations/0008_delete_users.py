# Generated by Django 4.1.2 on 2022-10-16 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petville', '0007_rename_getusers_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
