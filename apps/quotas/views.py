from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Control


# Create your views here.

def mostrar_fecha(request):
    return render(request, 'quotas/registro.html')


"""
class MostrarFecha(ListView):
    context_object_name = 'lista'
    template_name = 'quotas/registro.html'

    def get_queryset(self):
        f1 = self.request.GET.get('startDate', '')

        month = int(f1[:2])
        year = int(f1[3:len(f1)])
"""


def mostrar_fecha(request):
    f1 = request.GET.get('startDate', '')

    month = int(f1[:2])
    year = int(f1[3:len(f1)])

    control = Control.objects.get(user=request.user.userprofile)

    mes_pagado = control.pagado_hasta_month
    año_pagado = control.pagado_hasta_year

    context = {
        'mes_pagado': mes_pagado,
        'año_pagado': año_pagado,

        'month': month,
        'year': year
    }
    return render(request, 'quotas/registro.html', context)
