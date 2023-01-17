from rest_framework import serializers
from .models import Especialidades, Medico, Consulta, Cliente, Agenda

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Especialidades
        fields=['nome',]
class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medico
        fields=['nome','crm','email','telefone','especialidade',]

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=['first_name','email','password','username','cpf','sexo','telefone',]
class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agenda
        fields=['medico','dia','marcado',]
class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consulta
        fields=['cliente','data',]