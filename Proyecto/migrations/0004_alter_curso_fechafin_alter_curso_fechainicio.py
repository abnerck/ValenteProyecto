# Generated by Django 5.0.4 on 2024-04-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0003_alter_curso_tipocurso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='fechaFin',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='fechainicio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
