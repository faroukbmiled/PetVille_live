# Generated by Django 4.0 on 2022-10-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petville', '0038_remove_userdata_age_remove_userdata_dogname'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='per_what',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
