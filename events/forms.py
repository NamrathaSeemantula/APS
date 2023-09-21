from django import forms
from .models import events

class eventsForm(forms.ModelForm):

    class Meta():
        model = events
        fields = ('eventTopic', 'eventDesc', 'eventImg', 'eventDate', 'eventOrganizer')