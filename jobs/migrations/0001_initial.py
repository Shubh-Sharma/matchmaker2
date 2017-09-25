# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('flagged', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
                ('flagged', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='employer',
            name='location',
            field=models.ForeignKey(blank=True, to='jobs.Location', null=True),
        ),
    ]
