# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markupfield.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('started', models.DateTimeField(null=True, blank=True)),
                ('pre_reqs_completed', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='assignments')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('point_min', models.IntegerField(default=0)),
                ('point_max', models.IntegerField(default=0)),
                ('instructions', markupfield.fields.MarkupField(rendered_field=True)),
                ('instructions_markup_type', models.CharField(null=True, max_length=30, default=None, blank=True)),
                ('_instructions_rendered', models.TextField(editable=False)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='recipes')),
            ],
        ),
    ]
