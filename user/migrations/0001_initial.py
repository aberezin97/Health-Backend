# Generated by Django 4.0.5 on 2022-07-08 14:41

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('limit_calories', models.IntegerField(default=0)),
                ('limit_proteins', models.IntegerField(default=0)),
                ('limit_fats', models.IntegerField(default=0)),
                ('limit_carbohydrates', models.IntegerField(default=0)),
                ('goal_calories', models.IntegerField(default=0)),
                ('goal_proteins', models.IntegerField(default=0)),
                ('goal_fats', models.IntegerField(default=0)),
                ('goal_carbohydrates', models.IntegerField(default=0)),
                ('eaten_calories', models.IntegerField(default=0)),
                ('eaten_proteins', models.IntegerField(default=0)),
                ('eaten_fats', models.IntegerField(default=0)),
                ('eaten_carbohydrates', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('calories', models.DecimalField(decimal_places=1, default=0.0, max_digits=5)),
                ('proteins', models.DecimalField(decimal_places=1, default=0.0, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=1, default=0.0, max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=1, default=0.0, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
    ]
