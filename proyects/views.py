from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .models import Proyect
from .serializers import ProyectSerializer
from django.views.decorators.csrf import csrf_exempt


def vista_proyecto(request):
    if request.method == "POST":
        proyectos = request.POST.get('proyectos')
        rut = request.POST.get('rut')
        nombre_integrante = request.POST.get('nombre_integrante')

        # APLICAMOS QUE LOS DATOS INGRESADOS SE INTEGREN A LA BASE DE DATOS
        serializer = ProyectSerializer(data={
            'proyectos': proyectos,
            'rut': rut,
            'nombre_integrante': nombre_integrante
        })
        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse({'error': serializer.errors}, status=400)

        return redirect('vista_proyecto')

    projects = Proyect.objects.all()
    serializer = ProyectSerializer(projects, many=True)

    return render(request, 'html/index.html', {'projects': serializer.data})


@csrf_exempt
def eliminar_proyecto(request, project_id):
    try:
        project = Proyect.objects.get(id=project_id)
        project.delete()
        return redirect('vista_proyecto')
    except Proyect.DoesNotExist:
        return JsonResponse({'error': 'Proyecto no encontrado'}, status=404)


@csrf_exempt
def actualizar_proyecto(request, project_id):
    try:
        project = Proyect.objects.get(id=project_id)
        if request.method == "POST":
            proyectos = request.POST.get('proyectos')
            rut = request.POST.get('rut')
            nombre_integrante = request.POST.get('nombre_integrante')

            project.proyectos = proyectos
            project.rut = rut
            project.nombre_integrante = nombre_integrante
            project.save()

            return redirect('vista_proyecto')
        return render(request, 'html/update_project.html', {'project': project})
    except Proyect.DoesNotExist:
        return JsonResponse({'error': 'Proyecto no encontrado'}, status=404)
