from django.urls import path
from .views import *

urlpatterns = [
    path(
        '', 
        GenerarCodigoQRView.as_view(), 
        name='generar_codigo_qr'
    ),
    path(
        'recibir/', 
        RecibirArchivoView.as_view(), 
        name='recibir_archivo'
    ),
    path(
        'archivos/', 
        MostrarArchivosGuardadosView.as_view(),
        name='mostrar_archivos_guardados'
    ),
    path(
        'descargar/<int:archivo_id>/', 
        DescargarArchivoView.as_view(), 
        name='descargar_archivo'
    ),
    path(
        'archivos/<int:archivo_id>/vista-previa/', 
        VistaPreviaArchivoView.as_view(), 
        name='vista_previa_archivo'
    ),
    path(
        'archivos/<int:archivo_id>/vista-previa/', 
        VistaPreviaArchivoView.as_view(), 
        name='vista_previa_archivo'
    ),
    path(
        'eliminar-archivo/<int:pk>/', 
        EliminarArchivoView.as_view(), 
        name='eliminar_archivo'
    ),
]
