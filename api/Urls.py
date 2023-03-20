from django.urls import path
from .views import *

urlPatterns =[
    path('', getEvents),
    path('add/', addEvent),
    path('delete/<int:id>/', deleteEvent),
    path('update/<int:id>/', updateEvent),
]