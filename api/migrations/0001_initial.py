# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('value', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GupleStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('max_guples', models.IntegerField(default=10)),
            ],
        ),
        migrations.AddField(
            model_name='guplestore',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Plan'),
        ),
        migrations.AddField(
            model_name='guple',
            name='guple_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.GupleStore'),
        ),
    ]
