# Generated by Django 3.2.2 on 2021-07-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management', '0009_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_form',
            name='remaining_leave',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
