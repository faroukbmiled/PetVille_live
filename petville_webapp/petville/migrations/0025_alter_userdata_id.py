# Generated by Django 4.0 on 2022-10-21 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('petville', '0024_alter_userdata_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.AutoField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
