# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectidea', '0004_auto_20150824_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='category',
        ),
        migrations.AddField(
            model_name='idea',
            name='category',
            field=models.CharField(choices=[('Tech', 'Technology'), ('Environment', 'Environment'), ('Shopping', 'Shopping'), ('People', 'People'), ('Financial', 'Financial'), ('Writing', 'Writing')], default='Technology', max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
