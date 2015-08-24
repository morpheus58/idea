# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectidea', '0003_idea_similar_to_tweet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='similar_to_tweet',
        ),
        migrations.AddField(
            model_name='idea',
            name='sentiment',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
