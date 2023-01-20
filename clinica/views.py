from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .serializers import EspecialidadesSerializer,MedicoSerializer, ConsultaSerializer, ClienteSerializer, AgendaSerializer
from .models import Especialidades, Medico, Consulta, Cliente, Agenda
from datetime import date
import datetime
from rest_framework import permissions
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render,redirect
from validate_docbr import CPF
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
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
    from rest_framework import permissions
    serializer_class=ConsultaSerializer
    queryset=Consulta.objects.all()
    permission_classes = [permissions.IsAuthenticated]
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
        h=request.POST.get('marcado')
        busca=Agenda.objects.filter(medico=med).filter(dia=di)
        d=str(date.today())
        print('di',di)
        print('resultado da busca: ',busca)
        print('dia de hoje: ',d)
        data_compara=datetime.datetime.fromisoformat(di)
        hoje=datetime.datetime.fromisoformat(d)
        if(len(busca)<=0):
            if(hoje<=data_compara):
                medico=Medico.objects.get(id=int(med))
                a=Agenda(medico=Medico.objects.get(id=medico.id),dia=d,marcado=h)
                a.save()
                response='Agenda Criada para o médico '+medico.nome
            elif(len(busca)>0):
                response='agenda já feita para este dia!'
            elif(hoje>data_compara):
                response='data que você escolheu é anterior a atual!'
        else:
            response='Erro inesperado!'
            
        return Response(response)
# Create your views here.