# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectidea', '0005_auto_20150824_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='user',
        ),
    ]
