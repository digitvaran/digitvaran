# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_auto_20150211_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 21, 36, 35, 208766), help_text='Whern is the event going to happen?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 21, 36, 35, 208826), help_text='When do you want this published'),
            preserve_default=True,
        ),
    ]
