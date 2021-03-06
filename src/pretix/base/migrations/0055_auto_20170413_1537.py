# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-13 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0054_auto_20170413_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartposition',
            name='attendee_email',
            field=models.EmailField(blank=True, help_text='Empty, if this product is not an admission ticket', max_length=254, null=True, verbose_name='Attendee email'),
        ),
        migrations.AddField(
            model_name='orderposition',
            name='attendee_email',
            field=models.EmailField(blank=True, help_text='Empty, if this product is not an admission ticket', max_length=254, null=True, verbose_name='Attendee email'),
        ),
        migrations.AlterField(
            model_name='event_settingsstore',
            name='key',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='globalsettingsobject_settingsstore',
            name='key',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='organizer_settingsstore',
            name='key',
            field=models.CharField(max_length=255),
        ),
    ]
