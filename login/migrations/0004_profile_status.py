# Generated by Django 3.2.8 on 2021-10-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_profile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
