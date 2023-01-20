import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib import messages  # import messages

from .models import Control
from ..userprofile.models import UserProfile
from ..userprofile.forms import CustomUserForm


# Create your views here.

def get_date():
    current_date_time = datetime.datetime.now()
    date = current_date_time.date()
    actual_year = int(date.strftime("%Y"))
    actual_month = int(date.strftime("%m"))

    return actual_year, actual_month


def resumen(request):
    context = {}

    actual_year, actual_month = get_date()

    palabra_clave = request.GET.get('kword', )
    if palabra_clave:
        usuarios = UserProfile.objects.filter(
            Q(nombre__icontains=palabra_clave) | Q(id_veterinarian__icontains=palabra_clave)
        )
        for i in usuarios:
            us = UserProfile.objects.get(id=i.id)
            if int(actual_year) < int(us.activo_hasta_year):
                us.es_activo = True
            elif int(actual_year) > int(us.activo_hasta_year):
                us.es_activo = False
            else:
                if int(actual_month) <= int(us.activo_hasta_month):
                    us.es_activo = True
                else:
                    us.es_activo = False
            us.save()
    else:
        usuarios = UserProfile.objects.all()

    context['usuarios'] = usuarios

    return render(request, 'quotas/resumen.html', context)


def add_doctor(request):
    context = {}

    form = CustomUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Médico añadido correctamente")
        user = UserProfile.objects.last()

        return HttpResponseRedirect("/quotas/detail_doctor/" + str(user.id))

    context['form'] = form
    return render(request, "quotas/add_doctor.html", context)


def detail_doctor(request, pk):
    context = {}

    context["doctor"] = UserProfile.objects.get(id=pk)

    return render(request, "quotas/detail_doctor.html", context)


# update view for details
def update_doctor(request, pk):
    context = {}

    obj = get_object_or_404(UserProfile, id=pk)

    form = CustomUserForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/quotas/detail_doctor/" + str(pk))

    context["form"] = form

    return render(request, "quotas/update_doctor.html", context)


def mostrar_fecha(request, pk):

    f1 = request.POST.get('startDate', '')
    # idd = request.POST.get('id_veterinario', '')

    context = {}
    user = UserProfile.objects.get(id=pk)


    if request.method == 'POST':

        """
        try:
            user = UserProfile.objects.get(id=int(idd))
        except:
            user = None
            messages.warning(request, "Usuario no encontrado, corregir ID")

        if not user:
            #return render(request, 'quotas/pagar_quota.html')
            print("==================================")
            return redirect('pagar_quota')
        """

        if f1:
            month = int(f1[:2])
            year = int(f1[3:len(f1)])

            if year < user.pagado_hasta_year:
                messages.warning(request, "Fecha Incorrecta, Corregir Año")
                return HttpResponseRedirect(f'/quotas/pagar_quota/{user.id}')

            elif month <= user.pagado_hasta_month and year == user.pagado_hasta_year:
                messages.warning(request, "Fecha Incorrecta, Corregir Mes")
                return HttpResponseRedirect(f'/quotas/pagar_quota/{user.id}')


            user.pagado_hasta_month = month
            user.pagado_hasta_year = year


            if month + 2 > 12:
                year += 1
                month = (month + 2) % 12
            else:
                month += 2

            user.activo_hasta_month = month
            user.activo_hasta_year = year


            messages.success(request, "Pagado correctamente")
            user.save()

        #context['user'] = UserProfile.objects.get(id=int(idd))

    context['user'] = user

    return render(request, 'quotas/pagar_quota.html', context)
