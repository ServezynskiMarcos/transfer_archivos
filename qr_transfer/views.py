from django.shortcuts import render
import os
from django.http import HttpResponse
from .models import Archivo

def generar_codigo_qr(request):
    if request.method == 'GET':
        host = request.get_host()
        url = f'http://{host}/qr_transfer/recibir/'

        return render(request, 'mostrar_codigo_qr.html', {'url': url})

    return render(request, 'generar_codigo_qr.html')


def recibir_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo']
        guardar_archivo(archivo)

    return render(request, 'recibir_archivo.html')


def guardar_archivo(archivo):
    archivo_obj = Archivo(nombre=archivo.name, archivo=archivo.read())
    archivo_obj.save()


def mostrar_archivos_guardados(request):
  archivos = Archivo.objects.all()
  return render(request, 'mostrar_archivos.html', {'archivos': archivos})


def descargar_archivo(archivo_id):
    archivo_descargar = Archivo.objects.get(id=archivo_id)

    if archivo_descargar:
      response = HttpResponse(archivo_descargar.archivo, content_type='application/octet-stream')
      response['Content-Disposition'] = f'attachment; filename="{archivo_descargar.nombre}"'
      return response
    else:
      return HttpResponse("El archivo no existe.")
