# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liked_users', models.ManyToManyField(related_name='liked_users', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(related_name='liker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='liked_users',
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserLikes',
        ),
    ]
