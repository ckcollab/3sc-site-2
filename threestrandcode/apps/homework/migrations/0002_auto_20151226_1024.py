# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='module',
            field=models.CharField(default='github.SignUp', choices=[('github.SignUp', 'Sign up on Github'), ('github.MakeRepository', 'Make repository on Github'), ('github.MakeGHPage', 'Make GH page on GitHub')], max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions_markup_type',
            field=models.CharField(default=None, blank=True, choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain')], null=True, max_length=30),
        ),
    ]
