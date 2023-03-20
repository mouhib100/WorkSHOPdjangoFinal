from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Event.models import Event
from .serializers import EventSerializer

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status= status.HTTP_200_ok)


@api_view(['GET'])
def addEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def updateEvent(request, id=id):
    serializer = EventSerializer(instance=event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deleteEvent(request, id=id):
    try:
        event = Event.objects.get(id=id)
    except event.DoesNotExist:
        return Response(status="Event not found")
    event.delete()
    return Response(status="Event deleted")
