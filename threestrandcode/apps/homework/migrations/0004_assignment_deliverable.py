# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_auto_20151226_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='deliverable',
            field=models.URLField(null=True, blank=True),
        ),
    ]
