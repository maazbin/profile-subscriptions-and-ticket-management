# Generated by Django 4.1.5 on 2023-01-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_alter_subscriptiontype_advance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptiontype',
            name='advance',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subscriptiontype',
            name='basic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subscriptiontype',
            name='professional',
            field=models.BooleanField(default=False),
        ),
    ]