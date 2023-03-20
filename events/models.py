from django.db import models
from persons.models import Person
from datetime import date
from django.utils.timezone import  datetime
from django.core.validators import ValidationError
from django.core.validators import MinValueValidator
import re


#Controle de saisie de la date 
def isDateValid(value):
    if value <= date.today() :
        raise ValidationError('Invalid Date')
    return value    

#Controle de saisie du titre 
def isTitleValid(value):
    pattern ='[A-Z]+[a-z]+$'
    if not re.match(pattern, str(value)):
        raise ValidationError
    return value    

#model MVT
# Create your models here.
class Event(models.Model):
    Choice=(('MUSIQUE', 'MUSIQUE'), ('CINEMA','CINEMA' ), ('SPORT', 'SPORT'))  
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    category=models.CharField(max_length=8, choices=Choice)
    state=models.BooleanField(default=False)
    nbrParticipants=models.IntegerField(default=0, validators=[MinValueValidator(limit_value=0, message='Le nbr de participants doit etre positif')])
    dateEvent=models.DateField()
    #dateEvent=models.DateField(validators=[isDateValid])
    created_at=models.TimeField(auto_now_add=True)
    updated_at=models.TimeField(auto_now=True)

    #on va ici faire la liaison de Event avec Person(organizer) --> an organizer has many events --> on déclare le foreignKey de la table Person dans Event
    #blank --> 
    organizer = models.ForeignKey(Person, on_delete=models.CASCADE)
    #related name pour pouvoir accéder avec ce nom
    #ici on a déclaré la table associative entre les deux tables Event et Person(organizer), through --> le nom de la table associative
    participations=models.ManyToManyField(Person,related_name="participations",through="Participation")

    def __str__(self):
         return f" {self.title} and {self.state} " #personnalisation du dash 
    class Meta:
        constraints=[models.CheckConstraint(check=models.Q(dateEvent__gte=datetime.now()), name='date invalid')] #Q est un objet pour faire check avec ou, et,, xor, >, <
        verbose_name =('Evenement')
        verbose_name_plural ='Evenements'

             
            
        
class Participation(models.Model) :
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participationDate = models.DateTimeField(auto_now=True)
    class Meta: #une classe pour donner des infos supplementaires de la classe participation
        unique_together=('person','event')