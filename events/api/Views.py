from views import *

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
