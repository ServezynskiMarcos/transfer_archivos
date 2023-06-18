from django.urls import path
from . import views

urlpatterns = [
    path('', views.generar_codigo_qr, name='generar_codigo_qr'),
    path('recibir/', views.recibir_archivo, name='recibir_archivo'),
    path('archivos/', views.mostrar_archivos_guardados, name='mostrar_archivos_guardados'),
    path('descargar/<int:archivo_id>/', views.descargar_archivo, name='descargar_archivo'),
]
