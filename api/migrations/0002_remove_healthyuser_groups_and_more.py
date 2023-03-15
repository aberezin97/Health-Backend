# Generated by Django 4.0.5 on 2022-07-08 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthyuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='healthyuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='day',
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='HealthyUser',
        ),
        migrations.DeleteModel(
            name='Nutrition',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
