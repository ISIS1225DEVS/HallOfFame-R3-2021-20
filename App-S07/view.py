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

import config as cf
import sys
import controller
import prettytable as pt
from DISClib.ADT import orderedmap as om
import time
from prettytable import PrettyTable, ALL
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#===================
#Ruta a los archivos
#===================
ufosfile = 'UFOS//UFOS-utf8-large.csv'
cont = None

#==============
#Menú Principal
#==============
def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de ufos")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")
    print("8- Requerimiento 6")
    print("0- Salir")
    print("*******************************************")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')
    
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de ufos ....")
        controller.loadData(cont, ufosfile)
        
        total_ufos = lt.size(cont['ufos'])

        i = 1
        primeros_5 = lt.newList()
        while i <= 5:
            x = lt.getElement(cont['ufos'], i) 
            lt.addLast(primeros_5, x)
            i += 1

        j = 4
        ultimos_5 = lt.newList()
        while j >= 0:
            x = lt.getElement(cont['ufos'], total_ufos - j)
            lt.addLast(ultimos_5, x)
            j -= 1

        print('Casos de ufos cargados: ' + str(controller.ufosSize(cont)))
        
        print('The first 5 ufo cases are:')   

        tabla1 = pt.PrettyTable(['Datetime', 'City', 'State', 'Country', 'Shape', 'Duration (seconds)', 'Duration (hours/min)', 'Date Posted', 'Latitude', 'Longitude'])

        tabla1.max_width = 8

        for ufo in lt.iterator(primeros_5):
            tabla1.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)'], ufo['duration (hours/min)'], ufo['date posted'], ufo['latitude'], ufo['longitude']])

        tabla1.hrules = ALL

        print(tabla1)
        print('\n')

        print('The last 5 ufo cases are:')

        tabla2 = pt.PrettyTable(['Datetime', 'City', 'State', 'Country', 'Shape', 'Duration (seconds)', 'Duration (hours/min)', 'Date Posted', 'Latitude', 'Longitude'])

        tabla2.max_width = 8

        for obra in lt.iterator(ultimos_5):
            tabla2.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)'], ufo['duration (hours/min)'], ufo['date posted'], ufo['latitude'], ufo['longitude']])

        tabla2.hrules = ALL

        print(tabla2)
        print('\n')

        mapa1 = cont['cityIndex']
        mapa2 = cont['durationIndex']
        mapa3 = cont['timeIndex']
        mapa4 = cont['datetimeIndex']
        mapa5 = cont['longitudeIndex']
        
        start_time = time.process_time()

        requerimiento1 = controller.requerimiento1(mapa1, ufo)
        requerimiento2 = controller.requerimiento2(mapa2, ufo)
        requerimiento3 = controller.requerimiento3(mapa3, ufo)
        requerimiento4 = controller.requerimiento4(mapa4, ufo)
        requerimiento5 = controller.requerimiento5(mapa5, ufo)

        stop_time = time.process_time()

        elapsed_time_mseg = round((stop_time - start_time)*1000,2)

        print('El tiempo en el cual se cargan todos los datos es: ' + str(elapsed_time_mseg) + ' ms')
    
    elif int(inputs[0]) == 3:

        ciudad = input('Ingrese el nombre de la ciudad sobre la cual desea calcular los casos de ufos: \n>')
        ciudad_def = ciudad.lower()

        start_time = time.process_time()

        getUfos = controller.getUfosByCity(requerimiento1, ciudad_def)

        stop_time = time.process_time()

        elapsed_time_mseg = round((stop_time - start_time)*1000,2)

        print('El tiempo de procesamiento del requerimiento elegido es: ' + str(elapsed_time_mseg) + ' ms' + '\n')

        print('=============== Req No. 1 Inputs ===============')
        print('UFO Sightings in the city of ' + str(ciudad.upper()) + '\n')
        print('=============== Req No. 1 Answer ===============')
        print('There are ' + str(getUfos[0]) + ' different cities with UFO Sightings...' + '\n')

        print('There are ' + str(getUfos[1]) + ' sightings at the: ' + str(ciudad.upper()) + ' City')
        print('The first 3 and last 3 UFO sightings in the city are: ')

        tabla3 = pt.PrettyTable(['Datetime', 'City', 'State', 'Country', 'Shape', 'Duration (seconds)'])

        tabla3.max_width = 25

        for ufo in lt.iterator(getUfos[2]):
            tabla3.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)']])
    
        for ufo in lt.iterator(getUfos[3]):
            tabla3.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)']])

        tabla3.hrules = ALL

        print(tabla3)
    
    elif int(inputs[0]) == 4:

        limit_inf = input('Ingrese el límite inferior de duración en segundos: \n>')
        limit_sup = input('Ingrese el límite superior de duración en segundos: \n>')

        start_time = time.process_time()

        getUfos2 = controller.getUfosByDuration(requerimiento2, limit_inf, limit_sup)
    
        stop_time = time.process_time()

        elapsed_time_mseg = round((stop_time - start_time)*1000,2)

        print('El tiempo de procesamiento del requerimiento elegido es: ' + str(elapsed_time_mseg) + ' ms' + '\n')

        print('=============== Req No. 2 Inputs ===============')
        print('UFO Sightings between ' + str(limit_inf) + ' and ' + str(limit_sup) + ' seconds' + '\n')
        print('=============== Req No. 2 Answer ===============')
        print('There are ' + str(getUfos2[0]) + ' different UFO sightings durations...')
        print('The longest UFO sighting is: ')

        tabla4_1 = pt.PrettyTable(['Duration (seconds)', 'Count'])

        tabla4_1.max_width = 15
        tabla4_1.add_row([getUfos2[4], getUfos2[5]])
        tabla4_1.hrules = ALL
        print(tabla4_1)
        print('\n')

        print('There are ' + str(getUfos2[1]) + ' sightings between: ' + str(limit_inf) + ' and ' + str(limit_sup) + ' duration')
        print('The first 3 and last 3 UFO sightings in the duration time are: ')

        tabla4 = pt.PrettyTable(['Datetime', 'City', 'State', 'Country', 'Shape', 'Duration (seconds)'])

        tabla4.max_width = 25

        for ufo in lt.iterator(getUfos2[2]):
            tabla4.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)']])
    
        for ufo in lt.iterator(getUfos2[3]):
            tabla4.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)']])

        tabla4.hrules = ALL

        print(tabla4)
    
    elif int(inputs[0]) == 5:
        limit_inf = input('Ingrese el límite inferior de duración en el formato HH:MM \n>')
        limit_sup = input('Ingrese el límite superior de duración en el formato HH:MM \n>')
        start_time = time.process_time()

        getUfos3 = controller.getUfosByTime(requerimiento3, limit_inf, limit_sup)
    
        stop_time = time.process_time()

        elapsed_time_mseg = round((stop_time - start_time)*1000,2)

        print('El tiempo de procesamiento del requerimiento elegido es: ' + str(elapsed_time_mseg) + ' ms' + '\n')


        

        print('=============== Req No. 3 Inputs ===============')
        print('UFO Sightings between ' + str(limit_inf) + ' and ' + str(limit_sup) + '\n')
        print('=============== Req No. 3 Answer ===============')
        print('There are ' + str(getUfos3[0]) + ' UFO sightings with different times [hh-mm-ss]...')
        print('The latest UFO sightings time is: ')

        tabla5_1 = pt.PrettyTable(['Date', 'Count'])

        tabla5_1.max_width = 15
        
        tabla5_1.add_row([getUfos3[4], getUfos3[5]])
        tabla5_1.hrules = ALL
        print(tabla5_1)
        print('\n')

        print('There are ' + str(getUfos3[1]) + ' sightings between: ' + str(limit_inf) + ' and ' + str(limit_sup))
        print('The first 3 and last 3 UFO sightings in this time are: ')

        tabla5 = pt.PrettyTable(['Datetime', 'City', 'State', 'Country', 'Shape', 'Duration (seconds)'])

        tabla5.max_width = 25

        for ufo in lt.iterator(getUfos3[2]):
            tabla5.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)']])
    
        for ufo in lt.iterator(getUfos3[3]):
            tabla5.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)']])

        tabla5.hrules = ALL

        print(tabla5)

    elif int(inputs[0]) == 6:

        limit_inf = input('Ingrese el límite inferior de duración en el formato AAAA-MM-DD: \n>')
        limit_sup = input('Ingrese el límite superior de duración en el formato AAAA-MM-DD: \n>')

        start_time = time.process_time()

        getUfos4 = controller.getUfosByDatetime(requerimiento4, limit_inf, limit_sup)

        stop_time = time.process_time()

        elapsed_time_mseg = round((stop_time - start_time)*1000,2)

        print('El tiempo de procesamiento del requerimiento elegido es: ' + str(elapsed_time_mseg) + ' ms' + '\n')

        print('=============== Req No. 4 Inputs ===============')
        print('UFO Sightings between ' + str(limit_inf) + ' and ' + str(limit_sup) + '\n')
        print('=============== Req No. 4 Answer ===============')
        print('There are ' + str(getUfos4[0]) + ' different UFO sightings dates [YYYY-MM-DD]...')
        print('The oldest UFO sightings date is: ')

        tabla6_1 = pt.PrettyTable(['Date', 'Count'])

        tabla6_1.max_width = 15
        tabla6_1.add_row([getUfos4[4], getUfos4[5]])
        tabla6_1.hrules = ALL
        print(tabla6_1)
        print('\n')

        print('There are ' + str(getUfos4[1]) + ' sightings between: ' + str(limit_inf) + ' and ' + str(limit_sup))
        print('The first 3 and last 3 UFO sightings in this time are: ')

        tabla6 = pt.PrettyTable(['Datetime', 'City', 'State', 'Country', 'Shape', 'Duration (seconds)'])

        tabla6.max_width = 25

        for ufo in lt.iterator(getUfos4[2]):
            tabla6.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)']])
    
        for ufo in lt.iterator(getUfos4[3]):
            tabla6.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)']])

        tabla6.hrules = ALL

        print(tabla6)
    
    elif int(inputs[0]) == 7:

        lon_inf = input('Ingrese el limite inferior para la longitud (con 2 cifras decimales): \n>')
        lon_sup = input('Ingrese el limite superior para la longitud (con 2 cifras decimales): \n>')
        lat_inf = input('Ingrese el limite inferior para la latitud (con 2 cifras decimales): \n>')
        lat_sup = input('Ingrese el limite superior para la latitud (con 2 cifras decimales): \n>')

        start_time = time.process_time()

        getUfos5 = controller.getUfosByLonLat(requerimiento5, lon_inf, lon_sup, lat_inf, lat_sup)

        stop_time = time.process_time()

        elapsed_time_mseg = round((stop_time - start_time)*1000,2)

        print('El tiempo de procesamiento del requerimiento elegido es: ' + str(elapsed_time_mseg) + ' ms' + '\n')

        print('=============== Req No. 5 Inputs ===============')
        print('UFO Sightings between latitude range of ' + str(lat_inf) + ' and ' + str(lat_sup))
        print('plus longitude range of ' + str(lon_inf) + ' and ' + str(lon_sup) + '\n')
        print('=============== Req No. 5 Answer ===============')
        print('There are ' + str(getUfos5[0]) + ' different UFO sightings in the current area' + '\n')
        print('The first 5 and last 5 UFO sightings in this area are: ')

        tabla7 = pt.PrettyTable(['Datetime', 'City', 'State', 'Country', 'Shape', 'Duration (seconds)', 'Latitude', 'Longitude'])

        tabla7.max_width = 20

        for ufo in lt.iterator(getUfos5[1]):
            tabla7.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)'], ufo['latitude'], ufo['longitude']])
    
        for ufo in lt.iterator(getUfos5[2]):
            tabla7.add_row([ufo['datetime'], ufo['city'], ufo['state'], ufo['country'], ufo['shape'], ufo['duration (seconds)'], ufo['latitude'], ufo['longitude']])

        tabla7.hrules = ALL

        print(tabla7)
    
    elif int(inputs[0]) == 8:

        lon_inf = input('Ingrese el limite inferior para la longitud (con 2 cifras decimales): \n>')
        lon_sup = input('Ingrese el limite superior para la longitud (con 2 cifras decimales): \n>')
        lat_inf = input('Ingrese el limite inferior para la latitud (con 2 cifras decimales): \n>')
        lat_sup = input('Ingrese el limite superior para la latitud (con 2 cifras decimales): \n>')

        start_time = time.process_time()

        getUfos6 = controller.getUfosByLonLat(requerimiento5, lon_inf, lon_sup, lat_inf, lat_sup)

        latitud = (float(lat_inf)+float(lat_sup))/2
        longitud = (float(lon_inf)+float(lon_sup))/2
        mapa = controller.requerimiento6(latitud, longitud, getUfos6[3])
        mapa.save('mapita.html')

        stop_time = time.process_time()

        elapsed_time_mseg = round((stop_time - start_time)*1000,2)

        print('=============== Req No. 6 Inputs ===============')
        print('UFO Sightings between latitude range of ' + str(lat_inf) + ' and ' + str(lat_sup))
        print('plus longitude range of ' + str(lon_inf) + ' and ' + str(lon_sup) + '\n')
        print('=============== Req No. 6 Answer ===============')
        print('Check mapita.html')
    
    else:
        sys.exit(0)
sys.exit(0)
