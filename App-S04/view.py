"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """
import folium
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from datetime import date, time, datetime
import time
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar los avistamientos por Hora/Minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una zona geográfica")
    print("7- Visualizar los avistamientos de una zona geográfica")
    
catalogo = None


def cargarDatos(catalogo, datos):
    controller.cargarDatos(catalogo, datos)
    

archivo_datos = 'UFOS-utf8-80pct.csv'

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        
        catalogo = controller.initCatalogo()
        cargarDatos(catalogo, archivo_datos)
        print('2')
        

    elif int(inputs[0]) == 2:
        
        #Lab 8
        print('Altura del árbol: ', controller.alturaArbol(catalogo['ciudades']))
        print('Elementos en el árbol: ', controller.elementosArbol(catalogo['ciudades']))
        
        #Req 1
        
        ciudad = input('Contar los avistamientos en la ciudad de: ')
        
        info_ciudad = controller.infoCiudad(catalogo, ciudad)
        info_ciudad_ordenada = controller.llamarMerge(info_ciudad, identificador=1)
        primeros3 = lt.subList(info_ciudad_ordenada, 1, 3)
        ultimos3 = lt.subList(info_ciudad_ordenada, lt.size(info_ciudad_ordenada)-2, 3)
        cantidad_ciudades = controller.elementosArbol(catalogo['ciudades'])
        avistamientos_ciudad_ordenados = controller.llamarMerge(catalogo['avistamientos'], identificador = 2)
        ciudad_mayor = lt.firstElement(avistamientos_ciudad_ordenados)
        print('=====================================\n')
        print('Existen {} ciudades diferentes con avistamientos\n'.format(cantidad_ciudades))
        print('La ciudad con más avistamientos es: \n')
        print('    Ciudad    |    Número de avistamientos\n')
        print('{}     {}'.format(ciudad_mayor['ciudad'], ciudad_mayor['num_avistamientos']))        
        print('==================================================\n')
        print('Hay {} avistamientos en la ciudad: {}'.format(lt.size(info_ciudad_ordenada), ciudad))
        print('Los primeros y los últimos 3 avistamientos en la ciudad son: \n')
        print('    Fecha y hora    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración (segundos)')
        
        for i in lt.iterator(primeros3):
            print('{}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
        for i in lt.iterator(ultimos3):
            print('{}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
                    
    
    elif int(inputs[0]) == 3:
        ti = time.process_time()
        num_max = controller.llamarDarNumeroDuracionMaxima(catalogo)
        print(f'El número de avistamientos con el tiempo máximo de {num_max[1]} segundos es de: {num_max[0]}')
        print('==================================================\n')
        duracion_inicial = input('Digite la duración inicial: ')
        duracion_final = input('Digite la duración final: ')
        rango_duracion = controller.rangoLLaves(catalogo['duracion_segundos'], float(duracion_inicial), float(duracion_final)) 
        info_duracion1 = lt.newList(datastructure='ARRAY_LIST') 

        for i in lt.iterator(rango_duracion):
            info = controller.infoMap(catalogo['duracion_segundos'], i)
            
            for j in lt.iterator(info):
                lt.addLast(info_duracion1, j)

        info_duracion = controller.llamarMerge(info_duracion1, identificador = 5)
        primeros3 = lt.subList(info_duracion1, 1, 3)
        ultimos3 = lt.subList(info_duracion1, lt.size(info_duracion1)-2, 3)
        print(f'El total de avistamientos con una duración entre {duracion_inicial} y {duracion_final} es de: {lt.size(info_duracion)}')
        print(f'Los tres primeros y tres ultimos avistamientos entre {duracion_inicial} y {duracion_final} son:')
        print('    Fecha y hora    |    Hora    |    Ciudad    |    País    |    Forma    |    Duración    ')
        print('===========================================================================================================')
        
        for i in lt.iterator(primeros3):
            print('{}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['tiempo_hora'], i['ciudad'], i['pais'], i['forma'], i['duracion_segundos']))
            
        for i in lt.iterator(ultimos3):
            print('{}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['tiempo_hora'], i['ciudad'], i['pais'], i['forma'], i['duracion_segundos']))
        tf = time.process_time()
        print(f'El tiempo de ejecución fue de: {(tf-ti)*100} ms')


    elif int(inputs[0]) == 4:
        
        hora_inicial = input('Digite la hora inicial: ')
        hora_final_1 = input('Digite la hora final: ')
        hora_final_siguiente = hora_final_1.split(':')
        hora_final_siguiente[1] = str(int(hora_final_siguiente[1]) + 1)
        hora_final = hora_final_siguiente[0] + ':' + hora_final_siguiente[1]
        
        rango_horas = controller.rangoLLaves(catalogo['avistamientos_por_hora'], hora_inicial, hora_final)
        info_horas = lt.newList(datastructure='ARRAY_LIST')
        
        for i in lt.iterator(rango_horas):
            info = controller.infoMap(catalogo['avistamientos_por_hora'], i)
            
            for j in lt.iterator(info):
                lt.addLast(info_horas, j)
            
        info_hora_ordenada = controller.llamarMerge(info_horas, identificador=3)
        primeros3 = lt.subList(info_hora_ordenada, 1, 3)
        ultimos3 = lt.subList(info_hora_ordenada, lt.size(info_hora_ordenada)-2, 3)
        primerElemento = controller.obtenerMax(catalogo['avistamientos_por_hora'])
        #primerElemento = lt.lastElement(ultimos3)
        info_primer_elemento = controller.infoMap(catalogo['avistamientos_por_hora'], primerElemento)
         
        print('Existen {} avistamientos con diferentes tiempos\n'.format(controller.elementosArbol(catalogo['avistamientos_por_hora'])))
        print('El avistamiento más tardío es: \n')
        print('    Hora    |    Cantidad    \n')
        print('{}     {}\n'.format(primerElemento, lt.size(info_primer_elemento)))
        print('Existen {} avistamientos entre {} y {} \n'.format(lt.size(info_horas), hora_inicial, hora_final_1))
        print('    Fecha y hora    |    Hora    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración    ')
        print('===========================================================================================================')
        
        for i in lt.iterator(primeros3):
            print('{}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['tiempo_hora'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
            
        for i in lt.iterator(ultimos3):
            print('{}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['tiempo_hora'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
            
            
    elif int(inputs[0]) == 5:
        ti = time.process_time()
        fecha_antigua = controller.llamarDarNumeroFechaAntigua(catalogo)
        print(f'El Número de avistamientos en la fecha más antigua {fecha_antigua[1]} es de: {fecha_antigua[0]}')

        fecha_inicial = input('Digite la fecha inicial: ')
        fecha_final = input('Digite la fecha final: ')
        
        rango_fechas = controller.rangoLLaves(catalogo['fechas'], fecha_inicial, fecha_final)
        info_fechas = lt.newList(datastructure='ARRAY_LIST')
        
        for i in lt.iterator(rango_fechas):
            info = controller.infoMap(catalogo['fechas'], i)
            
            for j in lt.iterator(info):
                lt.addLast(info_fechas, j)
        
        info_fechas_ordenada = controller.llamarMerge(info_fechas, identificador=1)
        primeros3 = lt.subList(info_fechas_ordenada, 1, 3)
        ultimos3 = lt.subList(info_fechas_ordenada, lt.size(info_fechas_ordenada)-2, 3)
        print(f'El total de avistamientos con una fecha entre {fecha_inicial} y {fecha_final} es de: {lt.size(info_fechas_ordenada)}')
        
        print('    Fecha y hora    |    Fecha    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración    ')
        print('===========================================================================================================')
        
        for i in lt.iterator(primeros3):
            print('{}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['tiempo'].split()[0], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
            
        for i in lt.iterator(ultimos3):
            print('{}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['tiempo'].split()[0], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
        tf = time.process_time()
        print(f'El tiempo de ejecución fue de: {(tf-ti)*100} ms')


    elif int(inputs[0]) == 6:
        ti = time.process_time()
        lon_min = input('Digite la longitud minima: ')
        lon_max = input('Digite la longitud maxima: ')
        lat_min = input('Digite la latitud minima: ')
        lat_max = input('Digite la latitud maxima: ')

        rango_longitudes = controller.rangoLLaves(catalogo['longitud'], float(lon_min), float(lon_max))
        info_longitudes = lt.newList(datastructure='ARRAY_LIST')
        
        for i in lt.iterator(rango_longitudes):
            info = controller.infoMap(catalogo['longitud'], i)
            
            for j in lt.iterator(info):
                lt.addLast(info_longitudes, j)
        
        info_longitudes_rango = controller.llamarDarRangoLatitudes(info_longitudes, float(lat_min), float(lat_max))
        info_longitudes_ordenada = controller.llamarMerge(info_longitudes_rango, identificador=6)
        primeros5 = lt.subList(info_longitudes_ordenada, 1, 5)
        ultimos5 = lt.subList(info_longitudes_ordenada, lt.size(info_longitudes_ordenada)-4, 5)

        print(f'Existen {lt.size(info_longitudes_ordenada)} avistamientos en esa área')
        print('\n Los primeros 5 son: ')        
        print('    Fecha y hora    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración    |    Latitud    |    Longitud    ')
        print('===========================================================================================================')
        
        for i in lt.iterator(primeros5):
            print('{}    {}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos'], i['latitud'], i['longitud']))

        print('\n Los últimos 5 son: ')
        print('    Fecha y hora    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración    |    Latitud    |    Longitud    ')
        print('===========================================================================================================')
            
        for i in lt.iterator(ultimos5):
            print('{}    {}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos'], i['latitud'], i['longitud']))
        tf = time.process_time()
        print(f'El tiempo de ejecución fue de: {(tf-ti)*100} ms')
    
    elif int(inputs[0]) == 7:
        
        lon_min = input('Digite la longitud minima: ')
        lon_max = input('Digite la longitud maxima: ')
        lat_min = input('Digite la latitud minima: ')
        lat_max = input('Digite la latitud maxima: ')
        
        rango_longitudes = controller.rangoLLaves(catalogo['longitud'], float(lon_min), float(lon_max))
        info_longitudes = lt.newList(datastructure='ARRAY_LIST')
        
        for i in lt.iterator(rango_longitudes):
            info = controller.infoMap(catalogo['longitud'], i)
            
            for j in lt.iterator(info):
                lt.addLast(info_longitudes, j)
        
        info_longitudes_rango = controller.llamarDarRangoLatitudes(info_longitudes, float(lat_min), float(lat_max))
        info_longitudes_ordenada = controller.llamarMerge(info_longitudes_rango, identificador=6)
        primeros5 = lt.subList(info_longitudes_ordenada, 1, 5)
        ultimos5 = lt.subList(info_longitudes_ordenada, lt.size(info_longitudes_ordenada)-4, 5)

        print(f'Existen {lt.size(info_longitudes_ordenada)} avistamientos en esa área')
        print('\n Los primeros 5 son: ')        
        print('    Fecha y hora    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración    |    Latitud    |    Longitud    ')
        print('===========================================================================================================')
        
        for i in lt.iterator(primeros5):
            print('{}    {}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos'], i['latitud'], i['longitud']))

        print('\n Los últimos 5 son: ')
        print('    Fecha y hora    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración    |    Latitud    |    Longitud    ')
        print('===========================================================================================================')
            
        for i in lt.iterator(ultimos5):
            print('{}    {}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos'], i['latitud'], i['longitud']))
        
        
        lon_max = round(float(lon_max),2)
        lon_min = round(float(lon_min),2)
        lat_max = round(float(lat_max),2)
        lat_min = round(float(lat_min),2)
                   
        if  lon_max < 0 and lon_min < 0:
            longitud_map = (lon_max + lon_min)/2
            
        elif lon_max > 0 and lon_min > 0:
            longitud_map = (lon_max + lon_min)/2
            
        if  lat_max < 0 and lat_min < 0:
            latitud_map = (lat_max + lat_min)/2
        
        elif lat_max > 0 and lat_min > 0:
            latitud_map = (lat_max + lat_min)/2
            
            
        mapa = folium.Map(location=[latitud_map, longitud_map], zoom_start=6)
        
        for i in lt.iterator(primeros5):
            folium.Marker([i['latitud'], i['longitud']]).add_to(mapa)
            
        for j in lt.iterator(ultimos5):
            folium.Marker([j['latitud'], j['longitud']]).add_to(mapa)
        

        mapa.save('c:/Users/santi/OneDrive/Escritorio/Repositorios/Reto3-G07/Docs/mapa.html')
        
        
    else:
        sys.exit(0)
sys.exit(0)
