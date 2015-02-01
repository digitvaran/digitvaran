# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(help_text='A title in less than 30 characters', max_length=30)),
                ('details', models.CharField(help_text='A description in less than 500 characters', max_length=500)),
                ('event_date', models.DateField(help_text='Whern is the event going to happen?', default=datetime.datetime(2015, 2, 1, 12, 44, 35, 640933))),
                ('publish_date', models.DateTimeField(help_text='When do you want this published', default=datetime.datetime(2015, 2, 1, 12, 44, 35, 640996))),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('venue', models.CharField(help_text='A brief description of the venue if any', max_length=100, default='None')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notice',
            name='soc',
            field=models.ForeignKey(related_name='soc', to='notices.Society'),
            preserve_default=True,
        ),
    ]
