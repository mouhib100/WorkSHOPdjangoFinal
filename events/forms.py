# 1 --> on va utiliser les formulaires qui herite de Form 
# 2--> Model.Form --> on va faire a notre class Model Event, on peut utiliser le controle de saisie qu'on a deja creer
from django import forms
from .models import *
from django.views.generic import *

#from users.models import Person

class EventForm(forms.Form):
    title=forms.CharField(label='Title', max_length=9, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    description=forms.CharField(label='Event Description', widget=forms.Textarea(attrs={
        'class':'form-control'
    }))
    image=forms.ImageField(label='Event Image')
    category=forms.ChoiceField(choices=Event.Choice, widget=forms.RadioSelect)
    nbrParticipants=forms.IntegerField(min_value=0, step_size=1)
    dateEvent= forms.DateField(label='Event Date', widget=forms.DateInput(attrs={
        'type':'date',
        'class':'form-control date-input'
    }))
    organizer=forms.ModelChoiceField(label='Event Organizer',queryset=Person.objects.all())

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        #fields = '__all__'
        fields=['title', 'description', 'category', 'organizer', 'dateEvent','nbrParticipants', 'image']
        exclude=('state',)
    dateEvent= forms.DateField(label='Event Date', widget=forms.DateInput(attrs={
        'type':'date',
        'class':'form-control date-input'
    }))
    organizer=forms.ModelChoiceField(label='Event Organizer',queryset=Person.objects.all())

class DeleteEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = []


class EventModelFormPArticipation(forms.ModelForm):
    class Meta:
        model=Event
        fields=['participations']
        #exclude=('state',)     


