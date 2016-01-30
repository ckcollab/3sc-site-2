# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_assignment_deliverable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('path', models.ForeignKey(to='homework.Path', related_name='tracks')),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='point_max',
            new_name='points',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='point_min',
        ),
        migrations.AddField(
            model_name='recipe',
            name='required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='topic',
            field=models.ForeignKey(to='homework.Topic', related_name='topics'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='course',
            field=models.ForeignKey(related_name='recipes', default=1, to='homework.Course'),
            preserve_default=False,
        ),
    ]
