from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import  ValidationError
from django.core.validators import *




def mailValid(value):
    if not str(value).endswith('@esprit.tn'):
        raise ValidationError('Invalid mail ! Must ends with @esprit.tn')
    return value

def validLen(value):
    if len(value)!=8:
        raise ValidationError('Invalid cin ! Doit etre de longueur egale a 8')
        return value    

# Create your models here.
class Person (AbstractUser):
    cin=models.CharField(primary_key=True, max_length=255, validators=[MinLengthValidator(8, message='La valeur minimale doit etre superieure a 8'), MaxLengthValidator(8, message='La valeur maximale doit etre inferieure a 8')])
    email=models.EmailField(unique=True, max_length=255, validators=[mailValid])
    username=models.CharField(max_length=10, unique=True)
    USERNAME_FIELD='username' # ecraser le username par defaut et utiliser username declare
    def __str__(self):
        return f" {self.username} and {self.email} " #personnalisation du dash

    