# Generated by Django 4.0.3 on 2022-09-20 16:11

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=225, unique=True, verbose_name='URL')),
                ('category', models.CharField(choices=[('Account', 'Account'), ('Storage', 'Storage'), ('Market Place', 'Market Place')], max_length=50, verbose_name='Category of ticket')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Subject of ticker')),
                ('description', models.TextField(verbose_name='Description of question or issue')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2022, 9, 20, 19, 11, 13, 847255))),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Froze', 'Froze'), ('Close', 'Close')], default='Open', max_length=30, verbose_name='Status of ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=225, unique=True, verbose_name='URL')),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2022, 9, 20, 19, 11, 13, 847255))),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='support_api.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]