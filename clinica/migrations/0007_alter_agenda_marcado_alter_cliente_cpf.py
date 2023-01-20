# Generated by Django 4.1.5 on 2023-01-20 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0006_remove_agenda_horarios_agenda_marcado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='marcado',
            field=models.CharField(choices=[('1', '07:00-08:00'), ('2', '08:00-09:00'), ('3', '09:00-10:00'), ('4', '10:00-11:00'), ('5', '11:00-12:00'), ('6', '14:00-15:00'), ('7', '15:00-16:00'), ('8', '16:00-17:00')], max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=20, verbose_name='CPF'),
        ),
    ]