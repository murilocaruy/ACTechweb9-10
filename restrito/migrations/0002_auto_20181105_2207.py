# Generated by Django 2.0.6 on 2018-11-06 00:07

from django.db import migrations
import restrito.models.usuario


class Migration(migrations.Migration):

    dependencies = [
        ('restrito', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', restrito.models.usuario.UsuarioManager()),
            ],
        ),
    ]
