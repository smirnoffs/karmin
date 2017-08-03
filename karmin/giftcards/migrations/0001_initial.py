# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-02 21:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import karmin.giftcards.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.BigIntegerField(unique=True, validators=karmin.giftcards.models.maximum_10_symbols)),
                ('value', models.PositiveIntegerField(choices=[('50₴', 50), ('100₴', 100), ('200₴', 200), ('500₴', 500)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_at', models.DateTimeField(auto_now_add=True)),
                ('used_at', models.DateTimeField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftcards.GiftCard')),
                ('sold_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]