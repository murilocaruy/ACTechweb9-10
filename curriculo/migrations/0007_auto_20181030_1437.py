# Generated by Django 2.1.2 on 2018-10-30 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0006_disciplinasofertadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinasofertadas',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Curso'),
        ),
        migrations.AlterModelTable(
            name='disciplinasofertadas',
            table='DISCIPLINAOFERTADA',
        ),
    ]
