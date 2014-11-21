# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hermes', '0002_auto_20141121_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(unique=True, blank=True, default='', max_length='500'),
            preserve_default=True,
        ),
    ]
