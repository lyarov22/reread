# Generated by Django 4.2 on 2023-09-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reSite', '0008_booklisting_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklisting',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='listing_avatars/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatars/'),
        ),
    ]
