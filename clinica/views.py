from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .serializers import EspecialidadesSerializer,MedicoSerializer, ConsultaSerializer, ClienteSerializer, AgendaSerializer
from .models import Especialidades, Medico, Consulta, Cliente, Agenda
from datetime import datetime
from rest_framework.response import Response
class EspecialidadesViewSet(viewsets.ModelViewSet):
    serializer_class=EspecialidadesSerializer
    queryset=Especialidades.objects.all()

    def create(self, request):
        n=request.POST.get('nome')
        e=Especialidades(nome=n)
        e.save()
        return Response("Especialidade Salva!")
class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class=MedicoSerializer
    queryset=Medico.objects.all()
class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class=ConsultaSerializer
    def get_queryset(self):
        queryset=Consulta.objects.all()
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class=ClienteSerializer
    queryset=Cliente.objects.all()
class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class=AgendaSerializer
    queryset=Agenda.objects.all()
    def create(self, request):
        response=''
        med=request.POST.get('medico')
        di=request.POST.get('dia')
        h=request.POST.get('horarios')
        busca=Agenda.objects.filter(medico=med).filter(dia=di)
        d=datetime.now()
        dia=d.day
        print('day: ',dia)
        print('di',di)
        print('resultado da busca: ',busca)
        if(len(busca)<=0):
            medico=Medico.objects.get(id=int(med))
            a=Agenda(medico=Medico.objects.get(id=medico.id),dia=d,horarios=h)
            a.save()
            response='Agenda Criada para o médico ',medico.nome
        return Response(response)
# Create your views here.