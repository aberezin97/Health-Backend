# Generated by Django 4.0.5 on 2023-03-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='exercises',
            field=models.IntegerField(choices=[(0, 'NONE'), (1, 'READ'), (2, 'READWRITE')]),
        ),
        migrations.AlterField(
            model_name='permission',
            name='nutrition',
            field=models.IntegerField(choices=[(0, 'NONE'), (1, 'READ'), (2, 'READWRITE')]),
        ),
        migrations.AlterField(
            model_name='permission',
            name='weight',
            field=models.IntegerField(choices=[(0, 'NONE'), (1, 'READ'), (2, 'READWRITE')]),
        ),
    ]
