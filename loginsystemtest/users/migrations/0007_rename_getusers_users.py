# Generated by Django 3.2.6 on 2022-10-16 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20221016_1544'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GetUsers',
            new_name='Users',
        ),
    ]
