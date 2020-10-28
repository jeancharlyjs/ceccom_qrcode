#Django
from django.db import models
from django.contrib.auth.models import User

#Utilidades
import qrcode
import hashlib
from reportlab.pdfgen import canvas
from django.utils.text import slugify
from apps.utils.models import qrCeccomModels
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

#Models
from apps.perfilempresa.models import PerfilEmpresa

class PerfilVehiculo(qrCeccomModels, models.Model):

    CHASIS = RegexValidator(
            regex=r'\w[A-Z0-9]$',
            message="Requiere 17 digitos alfanumericos"
    )
    MATRICULA = RegexValidator(
            regex=r'\w[A-Z0-9]$',
            message="Requiere 6 digitos y una letra mayuscula"
    )

    registrado = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(PerfilEmpresa, on_delete=models.CASCADE)
    marca = models.CharField(
            _("Marca de Vehiculo"),
            blank=False,
            max_length=255,
            help_text=_("Registro de marca"),
            )
    chasis = models.CharField(
            _("Numero de Chasis"),
            max_length=17,
            blank=False,
            unique=True,
            validators=[CHASIS],
            error_messages={
                'unique':_("Chasis ya existe")
                },

    )
    matricula = models.CharField(
            _("Matricula"),
            max_length=6,
            blank=False,
            unique=True,
            validators=[MATRICULA],
            error_messages={
                'unique':_("Matricula ya existe")
                },
    )
    slug = models.SlugField(
            max_length=250,
            blank=True,
            unique=True,
            error_messages={
                'unique':_("Error")
                },
    )
    COLOR_VEHICULO = (
            ('R', 'Rojo'),
            ('A', 'Amarillo'),
            ('N', 'Negro'),
            ('AZ', 'Azul'),
            ('B', 'Blanco'),
    )
    color_vehiculo = models.CharField(
            _("Color Vehiculo"),
            max_length=3,
            blank=False,
            choices=COLOR_VEHICULO,
    )
    motor = models.CharField(
            _("Motor"),
            max_length=6,
            blank=False,
            unique=True,
            validators=[MATRICULA],
            error_messages={
                'unique':_("Motor ya existe")
                },
    )
    logopinture = models.ImageField(
            _("Vehiculos"),
            blank=False,
            upload_to="static/vehiculos",
    )

    url = models.ImageField(
            _("QRCode"),
            blank=True,
            upload_to="static/qrcode",
    )
    solicitud = models.CharField(
            _("Solicitud de Registro"),
            max_length=10,
            blank=False,
            unique=True,
            error_messages={
                'unique':_("La solicitud ya existe")
                },
    )
    fecha_servicio = models.DateTimeField(
            _("Fecha Puesta en Servicio"),
            auto_now_add=False,
            blank=True,

    )
    REMOLQUE = (
            ('R2', '2'),
            ('R3', '3'),
            ('R4', '4'),
    )
    remolque = models.CharField(
            _('Remolque'),
            max_length=2,
            blank=False,
            choices=REMOLQUE,
    )
    TIPO_GEOMETRICO = (
            ('C', 'Cilindrico'),
            ('E', 'Esferico'),
    )
    tipo_dimension = models.CharField(
            _('Tipo de Figura Geometrica'),
            max_length=1,
            blank=False,
            choices=TIPO_GEOMETRICO,

    )
    TIPO_COMBUSTIBLE = (
            ('G', 'Gas'),
            ('GN', 'Gas Natural'),
            ('GSL', 'Gasoil'),
    )
    tipocombustible = models.CharField(
            _("Tipo de Combustible"),
            blank=False,
            max_length=3,
            choices=TIPO_COMBUSTIBLE,

    )
    capacidad = models.IntegerField(
            _('Capacidad de Combustible'),
            blank=False
    )
    observacion = models.TextField(
            _('Otra observaciones'),
            blank=True,
            max_length=255,
    )
    def __str__(self):
        return self.chasis

    def get_absolute_url(self):
        from django.url import reverse
        return reverse('perfilvehiculo:vdetalles',
                        args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            #HASH PARA LOS SLUG, DONDE LA INFORMACION ESTARA ENCRIPTADA Y  EVITAR LA DUPLICIDAD.
            hash = hashlib.sha256()
            hash.update(('%s-%s'%(self.chasis, self.matricula)).encode('utf-8'))
            hashing = hash.hexdigest()
            self.slug = slugify(("%s"%(hashing)))
        super(PerfilVehiculo, self).save(*args, **kwargs)
        if not self.url:
            #PARA EL NOMBRE DEL DOMINIO SE DEBER ESPECIFICAR EL NOMBRE NO LA IP
            #DONDE PARA EL REGISTRO DE SLUG Y GENERAR LOS PDF Y PNG, SE DEBE TOMAR
            #EN CUENTA QUE LA URL ES DE QUIEN SE GENERA LOS ANTES DICHO.
            datos = f'http://10.0.0.5:8000/vehiculos/detalles/{self.slug}'
            #PENSAR QUE EN LA SIGUIENTE LINEA DEBE IR EL SLUG COMO
            #UNA URL
            self.url = slugify(self.slug)
            img = qrcode.make(datos)
            img.save("static/qrcode/CodigoQR_%s.png"%self.chasis)
            #GENERAR DOCUMENTOS PDF
            pdf = canvas.Canvas("static/documents_pdf/%s_%s-%s.pdf"%(self.empresa, self.matricula, self.chasis))
            pdf.drawInlineImage("static/ceccom.jpg", 90,650)
            pdf.drawInlineImage("static/qrcode/CodigoQR_%s.png"%self.chasis, 120,250, 400,400)
            pdf.drawString(250,230, "%s %s-%s"%(self.empresa, self.chasis, self.matricula))
            pdf.save()
            super(PerfilVehiculo, self).save(*args, **kwargs)
