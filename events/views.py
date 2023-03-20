from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Event
from .forms import *
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.

def HomePage(req, id):
    response ='hello from %s'
    return HttpResponse(response % id)

def eventStatic(req):
    list=[
        {'title':'title 1', 'description':'dictionnaire 1'},  # collection = dictionnaire en python
        {'title':'title 2', 'description':'dictionnaire 2'}
    ]    
    return render(req, 'events/staticList.html', {'events':list}) # render prend en parametre trois attrs --> request, nom de la template, context

def EventList(req):
    #list= Event.objects.all()
    list= Event.objects.filter(state=True)
    return render(req, 'events/EventList.html', {'events':list})    

def create_event(request):
    form = EventForm()
    if request.method == "POST":
        form= EventForm(request.POST, request.FILES)
        if form.is_valid():
            Event.objects.create(**form.cleaned_data) #** --> signifient tout les inputs
            return redirect('EventListClass')
        else:
            print(form.errors)
    return render(request, 'events/event_form.html', {'form':form})

def add_event(req):
    if req.method == "GET":
        form = EventModelForm()
        return render(req,"events/event_form.html", {'form':form})
    if req.method == "POST":
        form= EventModelForm(req.POST, req.FILES)
        if form.is_valid():
            Event = form.save(commit=False)
            Event.save()
            return redirect('EventListClass')
        else: 
            return render(req,"events/event_form.html", {'form':form})


        
class EventListClass (ListView):
    model=Event
    template_name='events/EventListView.html'
    context_object_name='events'  

    # def get_querysset(self):
    #     return Event.objects.filter(state=True)

class EventDetailsClass(DetailView):
    model=Event
    template_name='events/EventDetailView.html'
    context_object_name='event'

class CreateEvent(CreateView): # autre que ModelForm et Form
    model= Event
    template_name="events/event_form.html"
    form_class= EventModelForm
    success_url=reverse_lazy('EventListClass')    
class updateEvent(UpdateView):
    model= Event
    template_name="events/event_form.html"
    form_class= EventModelForm
    success_url=reverse_lazy('EventListClass')  


class ModelDeleteView(DeleteView):
    model=Event
    template_name='events/deleteEvent.html'
    success_url=reverse_lazy('eventLisClass')
class ModelDeleteParticipation(DeleteView):
    model=Event.participations
    template_name='events/deleteParticipation.html'
    success_url=reverse_lazy('eventLisClass')    
# class DeleteEventView(DeleteMessageMixin, FormView):
#     model = Event
#     form_class = DeleteEventForm
#     template_name = 'events/delete_event.html'
#     success_url = reverse_lazy('eventLisClass')
def increment_number(id, increment_by):
    # Retrieve the object from the database
    obj = Event.objects.get(id=id)

    # Increment the number
    obj.nbrParticipants += increment_by

    # Save the object with the new value
    obj.save()
def increment_numberParticipation(id, increment_by):
    # Retrieve the object from the database
    obj = Event.objects.get(id=id)

    # Increment the number
    obj.participations += increment_by

    # Save the object with the new value
    obj.save()    
def IncrementNbParticipants(req,id):
    event=Event.objects.get(id=id)
    increment_number(id, 1)
    count= event.participations.count()
    return HttpResponse(f"Le nombre de partipant pour levenement  {event.title} est incrementé par 1 {count} ")

def IncrementNbParticipation(req,id):
    event=Event.objects.get(id=id)
    increment_number(id, 1)
    return HttpResponse(f"Le nombre de participation pour levenement  {event.title} est incrementé par 1")   

             
 
class AddParticipation(UpdateView):
    model=Event
    template_name='events/createEvent.html'
    form_class=EventModelFormPArticipation
    success_url=reverse_lazy('EventListClass')  
class EventPartipations(DetailView):
    model=Event
    template_name='events/eventDetailClass.html'
    context_object_name='event' 
def supprimer_participation(request, id):
    evenement = get_object_or_404(Event, pk=id) #from django.shortcuts import get_object_or_404, redirect
    participation = get_object_or_404(Participation, event=evenement)
    participation.delete()
    return redirect('EventListClass', id=id)    
             

def createEventModelForm(req):
    if req.method=='GET':
        form=EventModelForm()
        return render(req,'events/createEvent.html',{'form':form})
    if req.method == 'POST':
        form=EventModelForm(req.POST, req.FILES)
        if form.is_valid():
            Event=form.save(commit=False)
            Event.save()
            return redirect('eventLisClass')
        else:
            return render(req,'events/createEvent.html',{'form':form})


class ModelDeleteView(DeleteView):
    model=Event
    template_name='events/deleteEvent.html'
    success_url=reverse_lazy('EventListClass')
class ModelDeleteParticipation(DeleteView):
    model=Event.participations
    template_name='events/deleteParticipation.html'
    success_url=reverse_lazy('EventListClass') 