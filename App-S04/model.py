"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import insertionsort as ist
from DISClib.Algorithms.Sorting import mergesort as mst
from DISClib.Algorithms.Sorting import quicksort as qst
from DISClib.Algorithms.Sorting import shellsort as sst
from datetime import date, time, datetime
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

lista_todas_ciudad = []
lista_ciudad = []

# Construccion de modelos

def initCatalogo():
    
    catalogo = {'datos':None,
                'ciudades': None,
                'fechas': None,
                'avistamientos': None,
                'avistamientos_por_hora': None,
                'duracion_segundos': None,
                'longitud': None
                }
    
    catalogo['datos'] = lt.newList(datastructure='ARRAY_LIST')
    catalogo['ciudades'] = om.newMap(omaptype='RBT')
    catalogo['fechas'] = om.newMap(omaptype='RBT')
    catalogo['avistamientos'] = lt.newList(datastructure='ARRAYLIST')
    catalogo['avistamientos_por_hora'] = om.newMap(omaptype='RBT')
    catalogo['duracion_segundos'] = om.newMap(omaptype='RBT')
    catalogo['longitud'] = om.newMap(omaptype='RBT')
    
    return catalogo
    


# Funciones para agregar informacion al catalogo

def agregarDato(catalogo, dato):
    
    dato = nuevoDato(dato)
    lt.addLast(catalogo['datos'], dato)
    agregarCiudad(catalogo['ciudades'], dato)
    agregarFechas(catalogo['fechas'], dato)
    agregarHoraAvistamiento(catalogo['avistamientos_por_hora'], dato)
    agregarDuracion(catalogo['duracion_segundos'], dato)
    agregarLongitud(catalogo['longitud'],dato)
    
    
def nuevoDato(dato):
    
    tiempo = dato['datetime']
    lista_hora = tiempo.split(' ')
    hora = lista_hora[1]
    
    nuevoDato = {'tiempo': dato['datetime'],
            'ciudad': dato['city'],
            'estado': dato['state'],
            'pais': dato['country'],
            'tiempo_hora': hora,
            'forma': dato['shape'],
            'duracion_segundos': dato['duration (seconds)'],
            'duracion_horas/minutos': dato['duration (hours/min)'], 
            'latitud': dato['latitude'],
            'longitud': dato['longitude']
            }
    
    return nuevoDato

def agregarDuracion(catalogo, dato):
    existe = om.contains(catalogo, float(dato['duracion_segundos']))

    if existe:        
        entry = om.get(catalogo, float(dato['duracion_segundos']))
        lista = me.getValue(entry)
        lt.addLast(lista, dato)
        
    else:
        lista = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista, dato)
        om.put(catalogo, float(dato['duracion_segundos']), lista)
    
def agregarLongitud(catalogo, dato):
    longitud = round(float(dato['longitud']), 2)
    latitud = round(float(dato['latitud']), 2)
    dato['latitud'] = latitud
    dato['longitud'] = longitud
    existe = om.contains(catalogo, longitud)

    if existe:
        entry = om.get(catalogo, longitud)
        lista = me.getValue(entry)
        lt.addLast(lista, dato)

    else:
        lista = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista, dato)
        om.put(catalogo, longitud, lista)
    
def agregarCiudad(catalogo, dato):
    
    existe = om.contains(catalogo, dato['ciudad'])
    lista_todas_ciudad.append(dato['ciudad'])
    
    if dato['ciudad'] not in lista_ciudad:
        lista_ciudad.append(dato['ciudad'])
    
    if existe:
        
        entry_ciudades = om.get(catalogo, dato['ciudad'])
        lista_ciudades = me.getValue(entry_ciudades)
        lt.addLast(lista_ciudades, dato)
        
    else:
        lista_ciudades = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista_ciudades, dato)
        om.put(catalogo, dato['ciudad'], lista_ciudades)
        
        
def agregarFechas(catalogo, dato):
    fecha = dato['tiempo'].split()

    existe = om.contains(catalogo, fecha[0])
    
    if existe:
        entry_fechas = om.get(catalogo, fecha[0])
        lista_fechas = me.getValue(entry_fechas)
        lt.addLast(lista_fechas, dato)
        
    else:
        lista_fechas = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista_fechas, dato)
        om.put(catalogo, fecha[0], lista_fechas)
        
        
def agregarHoraAvistamiento(catalogo, dato):
    
    hora = dato['tiempo_hora']
    existe = om.contains(catalogo, hora)
    
    if existe:
        entry_horas = om.get(catalogo, hora)
        lista_horas = me.getValue(entry_horas)
        lt.addLast(lista_horas, dato)
        
    else:
        lista_horas = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista_horas, dato)
        om.put(catalogo, hora, lista_horas)
    
        
def agregarAvistamientos(catalogo):
    
    lista = catalogo['avistamientos']
    
    for i in lista_ciudad:
        
        nuevoAvistamiento = {}
        cont = lista_todas_ciudad.count(i)
        
        nuevoAvistamiento['ciudad'] = i
        nuevoAvistamiento['num_avistamientos'] = cont
        
        lt.addLast(lista, nuevoAvistamiento)
    
    

# Funciones para creacion de datos

# Funciones de consulta

def alturaArbol(catalogo):
    return om.height(catalogo)


def elementosArbol(catalogo):
    return om.size(catalogo)


def infoCiudad(catalogo, ciudad):
    
    entry_ciudad = om.get(catalogo['ciudades'], ciudad)
    info_ciudad = me.getValue(entry_ciudad)
    
    return info_ciudad

def rangoLLaves(catalogo, hora_inicial, hora_final):
    return om.keys(catalogo, hora_inicial, hora_final)


def infoMap(catalogo, i):
    
    entry = om.get(catalogo, i)
    info = me.getValue(entry)
    return info

def darNumeroDuracionMaxima(catalogo):

    info_duracion = catalogo['duracion_segundos']
    max_key = om.maxKey(info_duracion)
    entry = om.get(catalogo['duracion_segundos'], max_key)
    max = me.getValue(entry)
    return lt.size(max), max_key

def darNumeroFechaAntigua(catalogo):
    info_fecha = catalogo['fechas']
    max_key = om.minKey(info_fecha)
    entry = om.get(catalogo['fechas'], max_key)
    max = me.getValue(entry)
    return lt.size(max), max_key

def darRangoLatitudes(lista_datos, lat_min, lat_max):
    lista = lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(lista_datos):
        lat = i['latitud']
        if lat < lat_max and lat > lat_min:
            lt.addLast(lista, i)
    return lista

def obtenerMax(catalogo):
    return om.maxKey(catalogo)


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpFechaAvistamiento(fecha1, fecha2):
    
    fecha1_final = datetime.strptime(fecha1['tiempo'], '%Y-%m-%d %H:%M:%S')
    fecha2_final = datetime.strptime(fecha2['tiempo'], '%Y-%m-%d %H:%M:%S')
    
    if fecha1_final < fecha2_final:
        return True
    else:
        return False
    
def cmpLatitud(latitud1, latitud2):

    l1 = latitud1['latitud']
    l2 = latitud2['latitud']

    if l1 < l2:
        return True
    else:
        return False

def cmpFechaAvistamientoPrueba(fecha1, fecha2):
    
    if fecha1 < fecha2:
        return True
    else:
        return False

def cmpDuracionCiudadPais(c1,c2):
    d1 = float(c1['duracion_segundos'])
    d2 = float(c2['duracion_segundos'])

    ciudad1 = c1['ciudad']
    ciudad2 = c2['ciudad']

    pais1 = c1['pais']
    pais2 = c2['pais']

    if d1 < d2:
        return True
    elif d1 == d2:
        if ciudad1 < ciudad2:
            return True
        elif ciudad1 == ciudad2:
            if pais1 < pais2:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

    
def cmpDuracionSegundos(duracion1,duracion2):

    duracion11 = int(duracion1['duracion_segundos'])
    duracion22 = int(duracion2['duracion_segundos'])

    if duracion11 < duracion22:
         return True
    else:
        return False
    
def cmpNumAvistamiento(av1, av2):
    
    av1_final = av1['num_avistamientos']
    av2_final = av2['num_avistamientos']
    
    if av1_final > av2_final:
        return True
    else: 
        return False
    
    
def cmpHoraAvistamiento(h1, h2):
    
    h1_final = h1['tiempo_hora']
    h2_final = h2['tiempo_hora']
    
    if h1_final < h2_final:
        return True
    elif h1_final == h2_final:
        
        fecha1 = h1['tiempo']
        fecha2 = h2['tiempo']
        
        return cmpFechaAvistamientoPrueba(fecha1, fecha2)
    
    else: 
        return False
    
    
    

# Funciones de ordenamiento

def insertion(datos, identificador): 
    
    if identificador == 1:
        lista_ordenada = ist.sort(datos, cmpFechaAvistamiento)
    elif identificador == 2:
        lista_ordenada = ist.sort(datos, cmpNumAvistamiento)
    elif identificador == 3:
        lista_ordenada = ist.sort(datos, cmpHoraAvistamiento)
    elif identificador == 4:
        lista_ordenada = ist.sort(datos, cmpDuracionSegundos)
    elif identificador == 5:
        lista_ordenada = ist.sort(datos, cmpDuracionCiudadPais)
    elif identificador == 6:
        lista_ordenada = ist.sort(datos, cmpLatitud)
    
    return lista_ordenada

def shell(datos, identificador):   
    
    if identificador == 1:
        lista_ordenada = sst.sort(datos, cmpFechaAvistamiento)
    elif identificador == 2:
        lista_ordenada = sst.sort(datos, cmpNumAvistamiento)
    elif identificador == 3:
        lista_ordenada = sst.sort(datos, cmpHoraAvistamiento)
    elif identificador == 4:
        lista_ordenada = sst.sort(datos, cmpDuracionSegundos)
    elif identificador == 5:
        lista_ordenada = sst.sort(datos, cmpDuracionCiudadPais)
    elif identificador == 6:
        lista_ordenada = sst.sort(datos, cmpLatitud)
    
    return lista_ordenada

def merge(datos, identificador):
    
    if identificador == 1:
        lista_ordenada = mst.sort(datos, cmpFechaAvistamiento)
    elif identificador == 2:
        lista_ordenada = mst.sort(datos, cmpNumAvistamiento)
    elif identificador == 3:
        lista_ordenada = mst.sort(datos, cmpHoraAvistamiento)
    elif identificador == 4:
        lista_ordenada = mst.sort(datos, cmpDuracionSegundos)
    elif identificador == 5:
        lista_ordenada = mst.sort(datos, cmpDuracionCiudadPais)
    elif identificador == 6:
        lista_ordenada = mst.sort(datos, cmpLatitud)
    
    return lista_ordenada

def quicksort(datos, identificador):
    
    if identificador == 1:
        lista_ordenada = qst.sort(datos, cmpFechaAvistamiento)
    elif identificador == 2:
        lista_ordenada = qst.sort(datos, cmpNumAvistamiento)
    elif identificador == 3:
        lista_ordenada = qst.sort(datos, cmpHoraAvistamiento)
    elif identificador == 4:
        lista_ordenada = qst.sort(datos, cmpDuracionSegundos)
    elif identificador == 5:
        lista_ordenada = qst.sort(datos, cmpDuracionCiudadPais)
    elif identificador == 6:
        lista_ordenada = qst.sort(datos, cmpLatitud)

    return lista_ordenada
