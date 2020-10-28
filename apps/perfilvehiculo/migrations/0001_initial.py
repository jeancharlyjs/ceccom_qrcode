# Generated by Django 3.0.7 on 2020-10-15 02:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfilempresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilVehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion', verbose_name='Creado en ')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha de modificacion', verbose_name='Modificado en ')),
                ('marca', models.CharField(help_text='Registro de marca', max_length=255, verbose_name='Marca de Vehiculo')),
                ('chasis', models.CharField(error_messages={'unique': 'Chasis ya existe'}, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Requiere 17 digitos alfanumericos', regex='\\w[A-Z0-9]{17}')], verbose_name='Numero de Chasis')),
                ('matricula', models.CharField(error_messages={'unique': 'Matricula ya existe'}, max_length=6, unique=True, validators=[django.core.validators.RegexValidator(message='Requiere 6 digitos', regex='\\w[A-Z]{01}[0-9]{05}')], verbose_name='Matricula')),
                ('slug', models.SlugField(blank=True, error_messages={'unique': 'Error'}, max_length=250, unique=True)),
                ('color_vehiculo', models.CharField(choices=[('R', 'Rojo'), ('A', 'Amarillo'), ('N', 'Negro'), ('AZ', 'Azul'), ('B', 'Blanco')], max_length=3, verbose_name='Color Vehiculo')),
                ('motor', models.CharField(error_messages={'unique': 'Motor ya existe'}, max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Requiere 17 digitos alfanumericos', regex='\\w[A-Z0-9]{17}')], verbose_name='Motor')),
                ('logopinture', models.ImageField(upload_to='static/vehiculos', verbose_name='Vehiculos')),
                ('url', models.ImageField(blank=True, upload_to='static/qrcode', verbose_name='QRCode')),
                ('solicitud', models.CharField(error_messages={'unique': 'La solicitud ya existe'}, max_length=10, unique=True, verbose_name='Solicitud de Registro')),
                ('fecha_servicio', models.DateTimeField(blank=True, verbose_name='Fecha Puesta en Servicio')),
                ('remolque', models.CharField(choices=[('R2', '2'), ('R3', '3'), ('R4', '4')], max_length=2, verbose_name='Remolque')),
                ('tipo_dimension', models.CharField(choices=[('C', 'Cilindrico'), ('E', 'Esferico')], max_length=1, verbose_name='Tipo de Figura Geometrica')),
                ('tipocombustible', models.CharField(choices=[('G', 'Gas'), ('GN', 'Gas Natural'), ('GSL', 'Gasoil')], max_length=3, verbose_name='Tipo de Combustible')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad de Combustible')),
                ('observacion', models.TextField(blank=True, max_length=255, verbose_name='Otra observaciones')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfilempresa.PerfilEmpresa')),
                ('registrado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
