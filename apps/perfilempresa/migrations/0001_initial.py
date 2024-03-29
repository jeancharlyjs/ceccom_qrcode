# Generated by Django 3.0.7 on 2020-10-15 02:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion', verbose_name='Creado en ')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha de modificacion', verbose_name='Modificado en ')),
                ('rnc', models.CharField(error_messages={'unique': 'El RNC o Cedula, ya existe'}, help_text='Requiere numero de RNC o Cedula ID registrada', max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Requiere 9 o 11 digitos', regex='\\d{11}')], verbose_name='RNC')),
                ('nombre', models.CharField(help_text='Registrar Nombre empresa', max_length=255, verbose_name='Nombr Empresa')),
                ('direccion', models.TextField(max_length=255, verbose_name='Direccion')),
                ('tipocombustible', models.CharField(choices=[('G', 'Gas'), ('GN', 'Gas Natural'), ('GSL', 'Gasoil'), ('GG', 'Gas/Gasolina'), ('GGG', 'Gas/Gasolina/Gasoil')], max_length=3, verbose_name='Tipo de Combustible')),
                ('slug', models.SlugField(blank=True, max_length=11, unique=True)),
                ('logopinture', models.ImageField(upload_to='static/logos', verbose_name='Logo Empresa')),
                ('estatus', models.CharField(choices=[('N', 'Normalizado'), ('I', 'Investigacion'), ('C', 'Claururada')], max_length=1, verbose_name='Estatus')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
