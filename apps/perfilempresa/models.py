#Django
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

#Utilidades
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from apps.utils.models import qrCeccomModels
from django.utils.text import slugify


class PerfilEmpresa(qrCeccomModels, models.Model):

    RNC = RegexValidator(
            regex=r'\d{11}',
            message="Requiere 9 o 11 digitos"
    )
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    rnc = models.CharField(
            _('RNC'),
            blank=False,
            max_length=11,
            unique=True,
            help_text=_("Requiere numero de RNC o Cedula ID registrada"),
            validators=[RNC],
            error_messages={
                'unique':_("El RNC o Cedula, ya existe")
            },
            )
    nombre = models.CharField(
            _("Nombr Empresa"),
            blank=False,
            max_length=255,
            unique=True,
            help_text=_("Registrar Nombre empresa"),
            )
    direccion = models.TextField(
            _("Direccion"),
            blank=False,
            max_length=255,
    )
    TIPO_COMBUSTIBLE = (
            ('G', 'Gas'),
            ('GN', 'Gas Natural'),
            ('GSL', 'Gasoil'),
            ('GG', 'Gas/Gasolina'),
            ('GGG', 'Gas/Gasolina/Gasoil'),
    )
    tipocombustible = models.CharField(
            _("Tipo de Combustible"),
            blank=False,
            max_length=3,
            choices=TIPO_COMBUSTIBLE,

    )
    slug = models.SlugField(
            max_length=11,
            blank=True,
            unique=True,
    )
    logopinture = models.ImageField(
            _("Logo Empresa"),
            blank=True,
            upload_to="static/logos"
    )

    STATUS = (
            ('N', "Normalizado"),
            ('I', "Investigacion"),
            ('C', "Clausurada"),
    )
    estatus = models.CharField(
            _("Estatus"),
            blank=False,
            max_length=1,
            choices=STATUS,
    )
    # coordenadas =
    def __str__(self):
        return self.nombre

    #URL para realizar mas detalles de un Empresa.
    def get_absolute_url(self):
        from django.url import reverse
        return reverse('perfilempresa:detalles',
                        args=[self.slug])

    #Guardar de forma automatica el slug tomando Nombre y RNC
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(("%s-%s"%(self.nombre, self.rnc)))
        super(PerfilEmpresa, self).save(*args, **kwargs)
