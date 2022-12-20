from django.db import models
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
        return self.medico.nome
class Cliente(models.Model):
    nome=models.CharField(max_length=200)
    cpf=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    sexo=models.CharField(max_length=5)
    telefone=models.CharField(max_length=30)
    def __str__(self):
        return self.nome
class Consulta(models.Model):
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agenda=models.ForeignKey(Agenda, on_delete=models.CASCADE)
    def __str__(self):
        return self.cliente.nome
        