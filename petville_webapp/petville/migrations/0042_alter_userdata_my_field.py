# Generated by Django 4.0 on 2022-10-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petville', '0041_userdata_my_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='my_field',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
