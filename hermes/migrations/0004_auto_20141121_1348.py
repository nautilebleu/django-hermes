# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hermes', '0003_auto_20141121_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-modified_on',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='hero',
        ),
    ]
