# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hermes.models


class Migration(migrations.Migration):

    dependencies = [
        ('hermes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length='500', default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='hero',
            field=models.ImageField(upload_to=hermes.models.post_hero_upload_to, blank=True, verbose_name='hero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='slug'),
            preserve_default=True,
        ),
    ]
