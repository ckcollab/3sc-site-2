# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20151226_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='recipe',
            field=models.ForeignKey(to='homework.Recipe', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions_markup_type',
            field=models.CharField(default='markdown', choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown')], editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='module',
            field=models.CharField(choices=[('github.SignUp', 'Sign up on Github'), ('github.MakeRepository', 'Make repository on Github'), ('github.MakeGHPage', 'Make GH page on GitHub')], max_length=128, unique=True),
        ),
    ]
