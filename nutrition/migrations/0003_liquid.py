# Generated by Django 4.0.5 on 2023-02-26 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_day_taken_liquid'),
        ('nutrition', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liquid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(null=True)),
                ('quantity', models.IntegerField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liquid', to='user.day')),
            ],
        ),
    ]