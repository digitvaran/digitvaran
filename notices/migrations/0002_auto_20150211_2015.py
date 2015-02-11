# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 11, 20, 15, 5, 975147), help_text='Whern is the event going to happen?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 11, 20, 15, 5, 975206), help_text='When do you want this published'),
            preserve_default=True,
        ),
    ]
