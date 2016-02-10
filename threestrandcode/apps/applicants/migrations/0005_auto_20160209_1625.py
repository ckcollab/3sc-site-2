# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0004_auto_20151225_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='applicant',
            name='last_name',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
