# Generated by Django 4.1.4 on 2023-01-02 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_consulta_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='agenda',
            new_name='data',
        ),
    ]
