# Generated by Django 4.1.2 on 2022-10-18 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petville', '0014_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='gender',
            new_name='dogname',
        ),
    ]
