# Generated by Django 3.2.8 on 2021-10-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_profile_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
