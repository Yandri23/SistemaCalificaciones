# Generated by Django 3.1.1 on 2020-10-03 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=10)),
                ('email', models.EmailField(default='@itsgg.edu.ec', max_length=254)),
                ('sexo', models.CharField(max_length=1)),
                ('estado', models.IntegerField(default=1)),
                ('user', models.CharField(max_length=15)),
                ('user_mod', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'docente',
                'verbose_name_plural': 'docentes',
                'db_table': 'tr_docente',
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=10)),
                ('email', models.EmailField(default='@itsgg.edu.ec', max_length=254)),
                ('sexo', models.CharField(max_length=1)),
                ('estado', models.IntegerField(default=1)),
                ('user', models.CharField(max_length=20)),
                ('user_mod', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'estudiante',
                'verbose_name_plural': 'estudiantes',
                'db_table': 'tr_estudiante',
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'grado',
                'verbose_name_plural': 'grados',
                'db_table': 'tr_grado',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
                'db_table': 'tr_materia',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.docente')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estudiante')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.grado')),
            ],
            options={
                'verbose_name': 'consulta',
                'verbose_name_plural': 'consultas',
                'db_table': 'tr_consulta',
            },
        ),
    ]
