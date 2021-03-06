# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_auto_20170929_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlike',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_users', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
