# Generated by Django 4.0 on 2022-10-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petville', '0040_alter_userdata_per_what'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='my_field',
            field=models.CharField(choices=[('dogsitter', 'Dog sitter'), ('catsitter', 'Cat sitter'), ('petgrooming', 'Pet Grooming'), ('dogwalking', 'Dog Walking'), ('catwalking', 'Cat Walking')], max_length=500, null=True),
        ),
    ]
