#Django
from django.db import models
from django.contrib.auth.models import User

#Utilidades
import qrcode
from reportlab.pdfgen import canvas
from django.utils.text import slugify
from apps.utils.models import qrCeccomModels
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

#Models
from apps.perfilempresa.models import PerfilEmpresa

class PerfilVehiculo(qrCeccomModels, models.Model):

    CHASI = RegexValidator(
            regex=r'\d{11}',
            message="Requiere 9 o 11 digitos"
    )
    MATRICULA = RegexValidator(
            regex=r'\d{6}',
            message="Requiere 6 digitos"
    )

    registrado = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(PerfilEmpresa, on_delete=models.CASCADE)
    marca = models.CharField(
            _("Marca de Vehiculo"),
            blank=False,
            max_length=255,
            help_text=_("Registro de marca"),
            )
    chasi = models.CharField(
            _("Numero de Chasi"),
            max_length=11,
            blank=False,
            unique=True,
            validators=[CHASI],
            error_messages={
                'unique':_("Chasi ya existe")
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
            max_length=50,
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
            max_length=11,
            blank=False,
            unique=True,
            validators=[CHASI],
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
        return self.chasi

    def get_absolute_url(self):
        from django.url import reverse
        return reverse('perfilvehiculo:vdetalles',
                        args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(("%s-%s-%s"%(self.empresa, self.matricula, self.chasi)))
        super(PerfilVehiculo, self).save(*args, **kwargs)
        if not self.url:
            datos = f'http://10.0.0.5:8000/vehiculos/detalles/{self.slug}'
            #PENSAR QUE EN LA SIGUIENTE LINEA DEBE IR EL SLUG COMO
            #UNA URL
            self.url = slugify(self.slug)
            img = qrcode.make(datos)
            img.save("static/qrcode/CodigoQR_%s.png"%self.chasi)
            #GENERAR DOCUMENTOS PDF
            pdf = canvas.Canvas("static/documents_pdf/%s_%s-%s.pdf"%(self.empresa, self.matricula, self.chasi))
            pdf.drawInlineImage("static/ceccom.jpg", 90,650)
            pdf.drawInlineImage("static/qrcode/CodigoQR_%s.png"%self.chasi, 80,200)
            pdf.drawString(250,200, "%s-%s"%(self.chasi, self.matricula))
            pdf.save()
            super(PerfilVehiculo, self).save(*args, **kwargs)
