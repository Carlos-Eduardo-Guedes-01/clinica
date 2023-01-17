# Generated by Django 4.1.5 on 2023-01-17 22:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0005_rename_agenda_consulta_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='horarios',
        ),
        migrations.AddField(
            model_name='agenda',
            name='marcado',
            field=models.CharField(choices=[('1', '07:00-08:00'), ('2', '08:00-09:00'), ('3', '09:00-10:00'), ('4', '10:00-11:00'), ('5', '11:00-12:00'), ('5', '14:00-15:00'), ('5', '15:00-16:00'), ('5', '16:00-17:00')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="O CPF precisa estar neste formato:                     '088.417.463-86'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('1', 'M'), ('2', 'F'), ('3', 'Per')], max_length=3),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=21, validators=[django.core.validators.RegexValidator(message="O número precisa estar neste formato:                         '+99 99 9999-0000'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefone'),
        ),
    ]
