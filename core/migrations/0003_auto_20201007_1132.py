# Generated by Django 3.1.1 on 2020-10-07 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201006_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materia',
            options={'ordering': ['materia'], 'verbose_name': 'materia', 'verbose_name_plural': 'materias'},
        ),
        migrations.AlterField(
            model_name='consulta',
            name='docente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.docente'),
        ),
    ]
