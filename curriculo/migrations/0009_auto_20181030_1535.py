# Generated by Django 2.1.2 on 2018-10-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0008_disciplinasofertadas_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinasofertadas',
            name='semestre',
            field=models.CharField(choices=[('PRIMEIRO', 'Primeiro Semestre'), ('SEGUNDO', 'Segundo Semestre'), ('TERCEIRO', 'Terceiro Semestre'), ('QUARTO', 'Quarto Semestre')], max_length=120, verbose_name='Semestre'),
        ),
    ]
