from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from control_estudios.forms import CursoFormulario, ProfesorFormulario, EntregableFormulario
from control_estudios.models import Estudiante, Curso, Profesor, Entregable


# NO USADO
# def listar_estudiantes(request):
#     contexto = {
#         "estudiantes": Estudiante.objects.all(),
#     }
#     http_response = render(
#         request=request,
#         template_name='control_estudios/lista_estudiantes.html',
#         context=contexto,
#     )
#     return http_response

# Vistas de cursos
def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response


def crear_curso_version_1(request):
    """No la estamos usando"""
    if request.method == "POST":
        data = request.POST  # es un diccionario
        nombre = data["nombre"]
        comision = data["comision"]
        curso = Curso(nombre=nombre, comision=comision)  # lo crean solo en RAM
        curso.save()  # Lo guardan en la Base de datos

        # Redirecciono al usuario a la lista de cursos
        url_exitosa = reverse('lista_cursos')  # estudios/cursos/
        return redirect(url_exitosa)
    else:  # GET
        http_response = render(
            request=request,
            template_name='control_estudios/formulario_curso_a_mano.html',
        )
        return http_response


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            comision = data["comision"]
            curso = Curso(nombre=nombre, comision=comision)  # lo crean solo en RAM
            curso.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_cursos')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Curso.objects.filter(comision__contains=busqueda)
        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_cursos.html',
            context=contexto,
        )
        return http_response


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.save()

            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
        }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario},
    )


def listar_profesor(request):
    contexto = {
        "profesores": Profesor.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_profesor.html',
        context=contexto,
    )
    return http_response



def crear_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            apellido = data["apellido"]
            dni = data["dni"]
            email = data['email']
            bio = data['bio']
            profesion = data["profesion"]
            profesor = Profesor(nombre=nombre, apellido=apellido, dni=dni, email=email, bio=bio, profesion=profesion)  # lo crean solo en RAM
            profesor.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_profesor')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_profesor.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_profesor(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        profesores = Profesor.objects.filter(dni__contains=busqueda)
        contexto = {
            "profesores": profesores,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_profesores.html',
            context=contexto,
        )
        return http_response


def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        profesor.delete()
        url_exitosa = reverse('lista_profesor')
        return redirect(url_exitosa)


def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.dni = data['dni']
            profesor.email = data['email']
            profesor.bio = data['bio']
            profesor.profesion = data['profesion']
            profesor.save()

            url_exitosa = reverse('lista_profesor')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'dni': profesor.dni,
            'email': profesor.email,
            'bio': profesor.bio,
            'profesion': profesor.profesion
        }
        formulario = ProfesorFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_estudios/formulario_profesor.html',
        context={'formulario': formulario},
    )



def listar_entregable(request):
    contexto = {
        "entregables": Entregable.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_entregable.html',
        context=contexto,
    )
    return http_response



def crear_entregable(request):
    if request.method == "POST":
        formulario = EntregableFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            fecha_entrega = data["fecha_entrega"]
            esta_aprobado = data["esta_aprobado"]
            entregable = Entregable(nombre=nombre, fecha_entrega=fecha_entrega, esta_aprobado=esta_aprobado)  # lo crean solo en RAM
            entregable.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_entregable')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = EntregableFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_entregable.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_entregable(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        entregables = Entregable.objects.filter(nombre__contains=busqueda)
        contexto = {
            "entregables": entregables,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_entregables.html',
            context=contexto,
        )
        return http_response


def eliminar_entregable(request, id):
    entregable = Entregable.objects.get(id=id)
    if request.method == "POST":
        entregable.delete()
        url_exitosa = reverse('lista_entregable')
        return redirect(url_exitosa)


def editar_entregable(request, id):
    entregable = Entregable.objects.get(id=id)
    if request.method == "POST":
        formulario = EntregableFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            entregable.nombre = data['nombre']
            entregable.fecha_entrega = data['fecha_entrega']
            entregable.esta_aprobado = data['esta_aprobado']
            entregable.save()

            url_exitosa = reverse('lista_entregable')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': entregable.nombre,
            'fecha_entrega': entregable.fecha_entrega,
            'esta_aprobado': entregable.esta_aprobado
        }
        formulario = EntregableFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_estudios/formulario_entregable.html',
        context={'formulario': formulario},
    )


# Vistas de Estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'control_estudios/lista_estudiantes.html'


class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni')
    success_url = reverse_lazy('lista_estudiantes')


class EstudianteDetailView(DetailView):
    model = Estudiante
    success_url = reverse_lazy('lista_estudiantes')


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni')
    success_url = reverse_lazy('lista_estudiantes')


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('lista_estudiantes')
