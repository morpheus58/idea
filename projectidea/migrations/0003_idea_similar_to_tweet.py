# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectidea', '0002_auto_20150824_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='similar_to_tweet',
            field=models.BooleanField(default=False),
        ),
    ]
