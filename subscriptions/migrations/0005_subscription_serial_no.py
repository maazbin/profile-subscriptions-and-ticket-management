# Generated by Django 4.1.5 on 2023-01-15 18:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_remove_subscriptiontype_advance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='serial_no',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]