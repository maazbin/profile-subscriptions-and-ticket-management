# Generated by Django 4.1.5 on 2023-01-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_alter_ticket_ticket_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_date',
            field=models.DateTimeField(default='2023-01-17'),
        ),
    ]