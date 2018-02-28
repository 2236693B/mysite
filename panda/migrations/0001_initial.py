# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 13:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('extract', models.CharField(default='Extract missing', max_length=500)),
                ('site', models.URLField(null=True)),
                ('date', models.DateField(null=True)),
                ('catergory', models.CharField(choices=[('NON', 'None'), ('ACT', 'Action'), ('ADV', 'Adventure'), ('ROL', 'Roleplaying'), ('MMO', 'MMO'), ('FPS', 'FPS'), ('SPO', 'SPO')], default='NON', max_length=3)),
                ('Playstation', models.BooleanField(default=False)),
                ('Xbox', models.BooleanField(default=False)),
                ('PC', models.BooleanField(default=False)),
                ('Nintendo', models.BooleanField(default=False)),
                ('Mobile', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GameRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panda.Game')),
            ],
        ),
        migrations.CreateModel(
            name='GameStudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.CharField(blank=True, max_length=200, null=True)),
                ('Steam', models.CharField(blank=True, max_length=31, null=True)),
                ('PSN', models.CharField(blank=True, max_length=16, null=True)),
                ('Xbox', models.CharField(blank=True, max_length=15, null=True)),
                ('Nintendo', models.CharField(blank=True, max_length=10, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gamerating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panda.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(blank=True, to='panda.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panda.GameStudio'),
        ),
    ]
