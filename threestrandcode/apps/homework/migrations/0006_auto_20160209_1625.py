# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0005_auto_20160130_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='topic',
            field=models.ForeignKey(to='homework.Topic', related_name='courses'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='path',
            field=models.ForeignKey(to='homework.Path', related_name='topics'),
        ),
    ]
