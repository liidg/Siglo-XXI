from django.shortcuts import render
from django.db import connection
import cx_Oracle
# Create your views here.

def index(request):
    return render(request, 'index.html')

def gestion(request):
    data = {	
        'ordenes': listado_ordenes(),
        'platos': listado_platos(),
    }

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        plato_id = request.POST.get('plato')
        salida = agregar_orden(nombre, precio, plato_id)
        if salida == 1:
            data['mensaje'] = 'Orden agregada correctamente'
            data['ordenes'] = listado_ordenes()
        else:
            data['mensaje'] = 'Error al agregar la orden'
    return render(request, 'gestion.html', data)

def listado_ordenes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_ORDENES", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def listado_platos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PLATOS", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def agregar_orden(nombre, precio, plato_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_ORDEN", [nombre, precio, plato_id, salida])
    return salida.getvalue()