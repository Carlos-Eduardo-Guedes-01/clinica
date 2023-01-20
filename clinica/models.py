from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

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
    h_choice=(("1", "07:00-08:00"),("2", "08:00-09:00"),("3", "09:00-10:00"),("4", "10:00-11:00"),("5", "11:00-12:00"),("6", "14:00-15:00"),("7", "15:00-16:00"),("8", "16:00-17:00"))
    marcado=models.CharField(max_length=30,choices=h_choice)
    
    def __str__(self):
        #string=str()
        return 'Dia '+str(self.dia)+' com médico '+str(self.medico.nome)+' ás '+str(self.marcado)
class Cliente(User):

    sx_choice=(('1','M'),('2','F'),('3','Per'))
    cpf=models.CharField(max_length=20, verbose_name='CPF')
    sexo=models.CharField(max_length=3,choices=sx_choice)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número precisa estar neste formato: \
                        '+99 99 9999-0000'.")
    telefone=models.CharField(max_length=21,verbose_name="Telefone",validators=[phone_regex])
    def __str__(self):
        return self.cliente.first_name
class Consulta(models.Model):
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data=models.ForeignKey(Agenda, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.cliente)+self.data