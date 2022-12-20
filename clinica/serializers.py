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
        fields=['nome','cpf','email','telefone','sexo',]
class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agenda
        fields=['medico','dia','horarios',]
class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consulta
        fields=['cliente','agenda',]