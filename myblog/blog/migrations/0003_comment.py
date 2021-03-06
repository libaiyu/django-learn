# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170724_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, verbose_name='昵称')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='文章')),
            ],
        ),
    ]
