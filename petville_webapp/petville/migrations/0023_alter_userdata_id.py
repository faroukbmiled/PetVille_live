# Generated by Django 4.0 on 2022-10-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petville', '0022_remove_profile_age_remove_profile_dogname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]