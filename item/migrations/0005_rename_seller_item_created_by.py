# Generated by Django 4.2.5 on 2024-05-13 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_item_options_rename_created_by_item_seller_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='seller',
            new_name='created_by',
        ),
    ]
