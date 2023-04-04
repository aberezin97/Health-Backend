# Generated by Django 4.0.5 on 2023-03-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_permission_user_a_remove_permission_user_b_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='stats',
            field=models.IntegerField(choices=[(0, 'NONE'), (1, 'READ'), (2, 'READWRITE')], default=0),
            preserve_default=False,
        ),
    ]