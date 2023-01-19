from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.resumen, name='resumen'),
    path('pagar_quota/', views.mostrar_fecha, name='pagar_quota'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('detail_doctor/<int:pk>', views.detail_doctor, name='detail_doctor'),
    path('update_doctor/<int:pk>', views.update_doctor, name='update_doctor'),
]
