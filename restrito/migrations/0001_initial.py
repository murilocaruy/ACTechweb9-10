# Generated by Django 2.1.2 on 2018-11-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=120, unique=True, verbose_name='Usuário')),
                ('data_expiracao', models.DateField(null=True, verbose_name='Data Expiração')),
                ('tipo', models.CharField(choices=[('C', 'Coordenador'), ('P', 'Professor'), ('A', 'Aluno')], max_length=1, verbose_name='Tipo de usuário')),
            ],
            options={
                'db_table': 'USUARIO',
            },
        ),
    ]
