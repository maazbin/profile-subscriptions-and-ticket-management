# Generated by Django 4.1.5 on 2023-01-16 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='date',
            new_name='ticket_date',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='id',
            new_name='ticket_id',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='status',
            new_name='ticket_status',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='user',
            new_name='user_id',
        ),
    ]
