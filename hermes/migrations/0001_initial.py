# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hermes.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.CharField(default='', max_length='500', blank=True)),
                ('parent', models.ForeignKey(null=True, blank=True, to='hermes.Category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('modified_on', models.DateTimeField(verbose_name='modified on', auto_now=True)),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug', unique=True)),
                ('summary', models.TextField(null=True, verbose_name='summary', blank=True)),
                ('body', models.TextField(verbose_name='body')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='hermes.Category', related_name='categories')),
            ],
            options={
                'ordering': ('-modified_on',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f', models.FileField(upload_to=hermes.models.postfile_upload_to)),
                ('post', models.ForeignKey(to='hermes.Post', related_name='files')),
            ],
            options={
                'verbose_name': 'PostFile',
                'verbose_name_plural': 'PostFiles',
            },
            bases=(models.Model,),
        ),
    ]
