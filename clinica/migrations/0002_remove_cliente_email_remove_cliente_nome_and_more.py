# Generated by Django 4.1.4 on 2022-12-29 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nome',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cliente',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agenda',
            name='dia',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=21),
        ),
    ]
