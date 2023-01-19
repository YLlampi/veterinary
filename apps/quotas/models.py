from django.db import models

from ..userprofile.models import UserProfile

# Create your models here.
class Control(models.Model):
    user = models.ForeignKey(UserProfile, related_name='control', on_delete=models.CASCADE)

    pagado_hasta_month = models.PositiveSmallIntegerField()
    pagado_hasta_year = models.PositiveSmallIntegerField()

    activo_hasta_month = models.PositiveSmallIntegerField()
    activo_hasta_year = models.PositiveSmallIntegerField()

    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.get_full_name()}'