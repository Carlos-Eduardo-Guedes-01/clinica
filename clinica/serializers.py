from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Especialidades, Medico, Consulta, Cliente, Agenda

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Especialidades
        fields=['nome',]
class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medico
        fields=['nome','crm','email','telefone','especialidade',]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','email','password','username',]
class ClienteSerializer(serializers.ModelSerializer):
    tracks=UserSerializer(many=True, read_only=True)
    class Meta:
        model=Cliente
        fields=['cpf','sexo','telefone','tracks']

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agenda
        fields=['medico','dia','horarios',]
class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consulta
        fields=['cliente','data',]