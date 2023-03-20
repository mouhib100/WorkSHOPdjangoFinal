from django.contrib import admin, messages
from .models import Event
from .models import Participation
from django.utils.timezone import  datetime


# Register your models here.


########################################################## Filtrer Par NB Participants ##########################################################
class ParticipantFilter(admin.SimpleListFilter):
    title='NBR Participants'
    parameter_name='nbrParticipants' # l'att avec lequel on va faire le filtre
    # les querySet et les lookups
    def lookups(self, request, model_admin):
        return (('0',("No Participants")),('more',("More Participants"))) #1er critere de recherche est 0
    def queryset(self, request, queryset):
        if self.value() == '0' :
            return queryset.filter(nbrParticipants__exact=0)
        if self.value() == 'more':
            return queryset.filter(nbrParticipants__gt=0)
########################################################## Filtrer Par NB Participants ##########################################################


################################################################ Filtrer Par Date ################################################################
class DateFiltre(admin.SimpleListFilter):
    title="Event Date"
    parameter_name='dateEvent'
    def lookups(self, request, model_admin):
            return (('Past Event',("Past Event")),
            ('Upcoming Event',("Upcoming Event")), 
            ('Today Event', ("Today Event"))) #1er critere de recherche est 0
    def queryset(self, request, queryset):
        if self.value() == 'Past Event':
            return queryset.filter(dateEvent__lt = datetime.today())
        if self.value() == 'Upcoming Event':
            return queryset.filter(dateEvent__gt = datetime.today())
        if self.value() == 'Today Event':
            return queryset.filter(dateEvent__exact = datetime.today())
################################################################ Filtrer Par Date ################################################################



################################################################ Participation inlines ###########################################################
class ParticipationInlines(admin.TabularInline): #StackedInline
    model= Participation
    extra=1 # Ajoute une seule fois le form de participation
    readonly_fields=('participationDate',) #date_participation
    can_delete= True
################################################################ Participation inlines ###########################################################


################################################################ Accept Event ###########################################################
def accept_events(model_admin,request,queryset):
        if model_admin.state==False:
            messages.error(request,message= " Oh No ")    
        rows_updated=queryset.update(state=True)
        if rows_updated ==1:
            msg="1 event"
        else:
            msg=f"{rows_updated} events"
        messages.success(request,message= "%s successfully accepted " %msg)
accept_events.short_description='Accept'
################################################################ Accept Event ###########################################################


################################################################ Refuse Event ###########################################################
def refuse_events(model_admin,request,queryset):
        rows_updated=queryset.update(state=False)
        if rows_updated ==1:
            msg="1 event"
        else:
            msg=f"{rows_updated} events"
        messages.success(request,message= "%s successfully Refused " %msg)
refuse_events.short_description='Refuse'
################################################################ Refuse Event ###########################################################

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def event_participants(self,obj):
        count =obj.participations.count()
        return count
    actions=[accept_events, refuse_events]
    list_display=('title','category','state','nbrParticipants','dateEvent')
    list_filter=('state','category',ParticipantFilter,DateFiltre)
    list_per_page =5
    ordering =('-title','category')
    search_fields=('title','category')
    readonly_fields=('created_at','updated_at')
    autocomplete_fields=('organizer',)
    fieldsets=(('State', { 'fields': ('state',)}),
                ('Event', { 
                           'classes' :('collapse',),
                           'fields': ('title', 'description','category' ,'nbrParticipants' ,'image','organizer')}),
                ('Dates', { 'fields': ('dateEvent','created_at','updated_at')})
               )
    inlines=[ParticipationInlines] #Personnalisation du form, extra est utilise pour avoir une seule ligne de form dans un autre form
class ParticipationsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Participation,ParticipationsAdmin)