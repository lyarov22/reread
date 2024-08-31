# Generated by Django 5.0.6 on 2024-08-31 06:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conversation', '0001_initial'),
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='item.item'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='members',
            field=models.ManyToManyField(related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversationmessage',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='conversation.conversation'),
        ),
        migrations.AddField(
            model_name='conversationmessage',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
