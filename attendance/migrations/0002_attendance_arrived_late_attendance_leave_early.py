# Generated by Django 4.0.5 on 2022-06-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='arrived_late',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendance',
            name='leave_early',
            field=models.BooleanField(default=False),
        ),
    ]
