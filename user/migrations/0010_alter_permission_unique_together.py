# Generated by Django 4.0.5 on 2023-03-04 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_permission_stats'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='permission',
            unique_together={('sender', 'receiver')},
        ),
    ]
