# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectidea', '0006_remove_idea_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='category',
            field=models.CharField(choices=[('Tech', 'Technology'), ('Environment', 'Environment'), ('Shopping', 'Shopping'), ('People', 'People'), ('Financial', 'Financial'), ('Writing', 'Writing')], max_length=20),
        ),
    ]
