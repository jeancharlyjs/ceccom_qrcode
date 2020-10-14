from django.db import models


class qrCeccomModels(models.Model):
    created = models.DateTimeField(
        'Creado en ',
        auto_now_add=True,
        help_text ="Fecha de creacion"
    )
    modified = models.DateTimeField(
        'Modificado en ',
         auto_now=True,
         help_text="Fecha de modificacion"
    )
    class Meta:
        abstract = True
        ordering = ['-created', '-modified']
        get_latest_by = 'created'
