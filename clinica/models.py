from django.db import models
from django.contrib.auth.models import User
class Especialidades(models.Model):
    nome=models.CharField(max_length=200)
    def __str__(self):
        return self.nome
class Medico(models.Model):
    nome=models.CharField(max_length=200)
    crm=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    telefone=models.CharField(max_length=30)
    especialidade=models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
class Agenda(models.Model):
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia=models.DateField(null=True)
    horarios=models.TimeField()
    def __str__(self):
        return str('Dia %s com médico %s'%(self.dia,self.medico))
class Cliente(User):
    #cliente=models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    cpf=models.CharField(max_length=20)
    sexo=models.CharField(max_length=3)
    telefone=models.CharField(max_length=21)
    USERNAME_FIELD='email'
    def __str__(self):
        return self.cliente.first_name
class Consulta(models.Model):
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data=models.ForeignKey(Agenda, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.cliente.first_name)