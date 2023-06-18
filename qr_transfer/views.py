from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, FormView, DeleteView
from .models import Archivo
from .forms import ArchivoForm


class GenerarCodigoQRView(View):
    """Vista que genera un codigo QR que te redirecciona a la view 
    RecibirArchivoView
    """
    def get(self, request):
        host = request.get_host()
        url = f'http://{host}/qr_transfer/recibir/'
        return render(request, 'mostrar_codigo_qr.html', {'url': url})


class RecibirArchivoView(FormView):
    """Vista que guarda el archivo cargado en la BDD y luego
    te redirecciona a la view MostrarArchivosGuardadosView
    """
    template_name = 'recibir_archivo.html'
    form_class = ArchivoForm
    success_url = reverse_lazy('mostrar_archivos_guardados')

    def form_valid(self, form):
        archivo = form.cleaned_data['archivo']
        existe = Archivo.objects.filter(nombre=archivo.name).exists()
        if existe:
            return redirect('mostrar_archivos_guardados')
        else:
            archivo_obj = Archivo(nombre=archivo.name,archivo=archivo.read())
            archivo_obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('Formulario inválido: No se ha seleccionado ningún archivo.')
        return super().form_invalid(form)


class MostrarArchivosGuardadosView(ListView):
    """Vista que lista los archivos almacenados en la BDD"""
    model = Archivo
    template_name = 'mostrar_archivos.html'
    context_object_name = 'archivos'


class VistaPreviaArchivoView(View):
    def get(self, request, archivo_id):
        archivo = get_object_or_404(Archivo, id=archivo_id)
        response = HttpResponse(content_type='image/jpeg')
        response.write(archivo.archivo)
        return response


class DescargarArchivoView(View):
    """Vista que descarga el archivo requerido"""
    def get(self, request, archivo_id):
        archivo_descargar = Archivo.objects.get(id=archivo_id)
        if archivo_descargar:
            response = HttpResponse(
                archivo_descargar.archivo, 
                content_type='application/octet-stream'
            )
            response['Content-Disposition'] = \
              f'attachment; filename="{archivo_descargar.nombre}"'
            return response
        else:
            return HttpResponse("El archivo no existe.")
        

class EliminarArchivoView(DeleteView):
    model = Archivo
    template_name = 'eliminar_archivo.html'
    success_url = reverse_lazy('mostrar_archivos_guardados')