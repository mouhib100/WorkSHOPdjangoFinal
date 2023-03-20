from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('homepage/<int:id>',HomePage, name='HomePage'), #<str:id>
    path('staticList',eventStatic, name='eventStatic'),
    path('eventList',EventList, name='EventList'),
    path('create_event/', create_event, name='CreateEvent'),
    path('add_event/', add_event, name='AddEvent'),
    path('listEventView',EventListClass.as_view(), name='EventListClass'),
    path('EventDetailView/<int:pk>',EventDetailsClass.as_view(), name='EventDetailsClass'),
    path('create_event_view', CreateEvent.as_view(), name='CreateEventView'), # asView --> path se pointe sur une classe et non pas une view
    path('update_event/<int:pk>',updateEvent.as_view(), name='UpdateEventView'),
    path('IncrementNbParticipants/<int:id>',IncrementNbParticipants,name='IncrementNbParticipants'),
    path('IncrementNbParticipation/<int:id>',IncrementNbParticipation,name='IncrementNbParticipation'),
    path('supprimer_participation/<int:id>/supprimer_participation/', supprimer_participation, name='supprimer_participation'),
    # path('ModelDeleteParticipation/',ModelDeleteParticipation.as_view(),name="ModelDeleteParticipation"),
    path('createEventModelForm',createEventModelForm,name="createEventModelForm"),
    path('ModelDeleteView/<int:pk>',ModelDeleteView.as_view(),name="ModelDeleteView"),
    path('AddParticipation/<int:pk>',AddParticipation.as_view(),name="AddParticipation"),
    path('EventPartipations/<int:pk>',EventPartipations.as_view(),name="EventPartipations"),
    path('ModelDeleteParticipation/',ModelDeleteParticipation.as_view(),name="ModelDeleteParticipation"),
    # path('DeleteEventView/<int:pk>',DeleteEventView.as_view(),name="DeleteEventView"),






]