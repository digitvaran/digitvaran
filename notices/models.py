from django.db import models
from django import forms
from django.utils import timezone

class Society(models.Model):
    "Society in college"
    name=models.CharField(max_length=50)
class Notice(models.Model):
    "A notice"
    title=models.CharField(max_length=30,help_text='A title in less than 30 characters')
    details=models.CharField(max_length=500,help_text='A description in less than 500 characters')

    event_date=models.DateField(default=timezone.now(),help_text='Whern is the event going to happen?')
    publish_date=models.DateTimeField(default=timezone.now(),help_text='When do you want this published')
    submit_date=models.DateTimeField(auto_now_add=True)

    venue=models.CharField(max_length=100,help_text='A brief description of the venue if any',default='None')
    soc=models.ForeignKey(Society,related_name='soc')
#---------------forms
class NoticeForm(forms.ModelForm):
    "A for for notices"
    class Meta:
        model=Notice
        exclude=['submit_date']
