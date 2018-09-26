# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-13 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelOptions(
            name='verifycode',
            options={'verbose_name': '短信验证码', 'verbose_name_plural': '短信验证码'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='电话'),
        ),
    ]
