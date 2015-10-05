# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.CharField(max_length=100, verbose_name=b'Comments')),
            ],
        ),
        migrations.CreateModel(
            name='template_name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.CharField(max_length=200, verbose_name=b'Template Name')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='template_name',
            field=models.ForeignKey(to='news.template_name'),
        ),
    ]
