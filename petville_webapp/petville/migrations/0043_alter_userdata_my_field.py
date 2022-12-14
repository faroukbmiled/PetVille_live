# Generated by Django 4.0 on 2022-10-25 14:29

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('petville', '0042_alter_userdata_my_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='my_field',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('dogsitter', 'Dog sitter'), ('catsitter', 'Cat sitter'), ('petgrooming', 'Pet Grooming'), ('dogwalking', 'Dog Walking'), ('catwalking', 'Cat Walking')], max_length=500, null=True),
        ),
    ]
