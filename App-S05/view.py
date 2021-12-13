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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
import prettytable
from prettytable import PrettyTable
import datetime
assert cf
import time as tm
import csv
import os



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- (Req 1) Contar los avistamientos en una ciudad")
    print("3- (Req 2) Contar los avistamientos por duración")    
    print("4- (Req 3) Contar los avistamientos por Hora/Minutos del día")    
    print("5- (Req 4) Contar los avistamientos en rango de fechas") 
    print("6- (Req 5) Contar los avistamientos de una Zona Geográfica")       
    print("0- Salir de la aplicacion")

catalog = None

# Funciones para la impresión de tablas

def PrintTopCities(city, count):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["City", "Count"]
    x.add_row([city, count])
    print(x)

def PrintTopDuration(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["Duration (seconds)", "Count"]
    x.add_row([info["duration"], info["size"]])
    print(x)

def PrintTopTime(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["Time", "Count"]
    x.add_row([info["time"], info["size"]])
    print(x)

def PrintTopDate(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["Date", "Count"]
    x.add_row([info["date"], info["size"]])
    print(x)

def printUfosTable(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["Datetime", "City", "State", "Country", "Shape", "Duration (seconds)"]
    for i in lt.iterator(info):
        x.add_row([ i["datetime"], i["city"], 
                    i["state"], i["country"], 
                    i["shape"], i["duration (seconds)"]])
    print(x)

def printLastTable(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["Datetime", "City", "State", "Country", "Shape", "Duration (seconds)", 'Latitude', 'Longitude']
    for i in lt.iterator(info):
        x.add_row([ i["datetime"], i["city"], 
                    i["state"], i["country"], 
                    i["shape"], i["duration (seconds)"], i["latitude"], i["longitude"]])
    data = x.get_string()
    inf = [tuple(filter(None, map(str.strip, splitline))) for line in data.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
    with open('Maps\locations.csv', 'w') as locations:
        writer = csv.writer(locations)
        writer.writerows(inf)
    print(x)

            

def PrintReq1(cityname, top, cityinfo):
    print("="*15, " Req No. 1 Inputs ", "="*15)
    print("UFO Sightings in the city of:", cityname,"\n")
    print("="*15, " Req No. 1 Answer ", "="*15)
    print("There are", top[2], "different cities with UFO sightings...")
    print("The city with most UFO sightings is:")
    PrintTopCities(top[0], top[1])
    print("\nThere are",cityinfo[1],"sightings at the:", cityname,"city")

    if lt.size(cityinfo[0]) > 6:
        first = controller.getFirst(cityinfo[0], 3)
        last = controller.getLast(cityinfo[0], 3)
        ltUfos = controller.FirtsAndLast(first, last)
        print('The first and last 3 UFO sightings in the city are:')
        printUfosTable(ltUfos)
        
    else:
        print('The UFO sightings in the city are:')
        printUfosTable(cityinfo[0])

def PrintReq2 (InRange, inf, sup, top):
    print("="*15, " Req No. 2 Inputs ", "="*15)
    print("UFO Sightings between:", inf, "and", sup ,"\n")
    print("="*15, " Req No. 2 Answer ", "="*15)
    print("There are", top[1], "different UFO sightings durations...\n")
    print("The longest UFO sighting duration(seconds) is:")
    PrintTopDuration(top[0])
    print("\nThere are", InRange[1],"sightings between", inf, "and", sup, "duration.")

    if InRange[1] > 6:
        first = controller.getFirst(InRange[0], 3)
        last = controller.getLast(InRange[0], 3)
        ltUfos = controller.FirtsAndLast(first, last)
        print('The first and last 3 UFO sightings in the duration time:')
        printUfosTable(ltUfos)
        
    else:
        print('The UFO sightings in the duration time:')
        printUfosTable(InRange[0])

def PrintReq3(InRange, inf, sup, top):
    print("="*15, " Req No. 3 Inputs ", "="*15)
    print("UFO Sightings between:", inf, "and", sup ,"\n")
    print("="*15, " Req No. 3 Answer ", "="*15)
    print("There are", top[1], "different UFO sightings times [HH:MM:SS]")
    print("The latest UFO sighting time is:")
    PrintTopTime(top[0])
    print("There are", InRange[1], "sightings between:", inf, "and", sup)
    if InRange[1] > 6:
        first = controller.getFirst(InRange[0], 3)
        last = controller.getLast(InRange[0], 3)
        ltUfos = controller.FirtsAndLast(first, last)
        print('The first and last 3 UFO sightings in this time are:')
        printUfosTable(ltUfos)
    else:
        print('The UFO sightings in this time are:')
        printUfosTable(InRange[0])

def PrintReq4(InRange, inf, sup, top):
    print("="*15, " Req No. 4 Inputs ", "="*15)
    print("UFO Sightings between:", inf, "and", sup ,"\n")
    print("="*15, " Req No. 4 Answer ", "="*15)
    print("There are", top[1], "different UFO sightings dates [YYYY-MM-DD]")
    print("The oldest UFO sighting date is:")
    PrintTopDate(top[0])
    print("There are", InRange[1], "sightings between:", inf, "and", sup)
    if InRange[1] > 6:
        first = controller.getFirst(InRange[0], 3)
        last = controller.getLast(InRange[0], 3)
        ltUfos = controller.FirtsAndLast(first, last)
        print('The first and last 3 UFO sightings in this time are:')
        printUfosTable(ltUfos)
    else:
        print('The UFO sightings in this time are:')
        printUfosTable(InRange[0])

def PrintReq5 (InRange, infLatitud, supLatitud, infLongitud, supLongitud):
    print("="*15, " Req No. 5 Inputs ", "="*15)
    print("UFO Sightings between latitude range:", infLatitud, "and", supLatitud)
    print("plus longitude range:", infLongitud, "and", supLongitud ,"\n")
    print("="*15, " Req No. 5 Answer ", "="*15)
    print("There are", InRange[1], "different UFOS sightings in the current area")
    if InRange[1] > 10:
        first = controller.getFirst(InRange[0], 5)
        last = controller.getLast(InRange[0], 5)
        ltUfos = controller.FirtsAndLast(first, last)
        print('The first and last 5 UFO sightings in this time are:')
        printLastTable(ltUfos)

    elif InRange[1] != 0:
        print('The UFO sightings in this time are:')
        printLastTable(InRange[0])

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        start = tm.process_time()

        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)

        end = tm.process_time()
        total_time = (end - start)

        print('Avistamientos cargadas:', controller.UfosSize(catalog))

        print('\nAltura del arbol de cityIndex:', controller.indexHeight(catalog,'cityIndex'))
        print('Elementos en el arbol de cityIndex:',controller.indexSize(catalog, 'cityIndex'))

        print('\nAltura del arbol de durationIndex:', controller.indexHeight(catalog,'durationIndex'))
        print('Elementos en el arbol de durationIndex:',controller.indexSize(catalog, 'durationIndex'))

        print('\nAltura del arbol de timeIndex:', controller.indexHeight(catalog,'timeIndex'))
        print('Elementos en el arbol de timeIndex:',controller.indexSize(catalog, 'timeIndex'))

        print('\nAltura del arbol de dateIndex:', controller.indexHeight(catalog,'dateIndex'))
        print('Elementos en el arbol de dateIndex:',controller.indexSize(catalog, 'dateIndex'))

        print('\nAltura del arbol de latitudeIndex:', controller.indexHeight(catalog,'latitudeIndex'))
        print('Elementos en el arbol de latitudeIndex:',controller.indexSize(catalog, 'latitudeIndex'))

        first = controller.getFirst(catalog['Ufos'], 5)
        last = controller.getLast(catalog['Ufos'], 5)
        ufos = controller.FirtsAndLast(first,last)
        print('\nThe first and last 5 UFO sightings loaded:')
        printUfosTable(ufos)

        print("The time it took to execute the requirement was:", total_time*1000 ,"mseg ->",total_time, "seg\n")

    elif int(inputs[0]) == 2: #Req 1
        cityname = input('Ingrese la ciudad: ')

        start = tm.process_time()
        cityinfo = controller.getUFOByCity(catalog, cityname.lower())

        if not cityinfo:
            print("La ciudad ingresada no tiene avistamientos de UFO\n")
            continue

        topcities = controller.getUFOTopCity(catalog)

        end = tm.process_time()
        total_time = (end - start)

        PrintReq1(cityname, topcities, cityinfo) 
        print("The time it took to execute the requirement was:", total_time*1000 ,"mseg ->",total_time, "seg\n")

    elif int(inputs[0]) == 3: #Req 2 - Valeria Caro
        minimo = float(input('Ingrese el valor minimo: '))
        maximo = float(input('Ingrese el valor maximo: '))

        start = tm.process_time()

        duration = controller.getUFOTopDuration(catalog)
        dur = controller.getUFOByDuration(catalog, minimo, maximo)

        end = tm.process_time()
        total_time = (end - start)

        PrintReq2(dur, minimo, maximo, duration)
        print("The time it took to execute the requirement was:", total_time*1000 ,"mseg ->",total_time, "seg\n")


    elif int(inputs[0]) == 4: #Req 3 - Sofia Velasquez
        inicial = input("Ingresa el tiempo inicial (HH:MM): ")
        final = input("Ingresa el tiempo final (HH:MM): ")
        inf = datetime.datetime.strptime(inicial, '%H:%M').time()
        sup = datetime.datetime.strptime(final, '%H:%M').time()

        start = tm.process_time()

        InRange = controller.getUFOinTime(catalog, inf, sup)    
        top5 = controller.getTopTime(catalog)

        end = tm.process_time()
        total_time = (end - start)

        PrintReq3(InRange, inf, sup, top5)
        print("The time it took to execute the requirement was:", total_time*1000 ,"mseg ->",total_time, "seg\n")
    
    elif int(inputs[0]) == 5: #Req 4
        inicial = input("Ingresa la fecha inicial (AAAA-MM-DD): ")
        final = input("Ingresa la fecha final (AAAA-MM-DD): ")
        inf = datetime.datetime.strptime(inicial, '%Y-%m-%d').date()
        sup = datetime.datetime.strptime(final, '%Y-%m-%d').date()

        start = tm.process_time()

        InRange = controller.getUFOinDate(catalog, inf, sup)    
        top5 = controller.getTopDate(catalog)

        end = tm.process_time()
        total_time = (end - start)

        PrintReq4(InRange, inf, sup, top5)
        print("The time it took to execute the requirement was:", total_time*1000 ,"mseg ->",total_time, "seg\n")
    
    elif int(inputs[0]) == 6: #Req 5
        infLatitud = round(float(input("Ingresa la latitud minima: ")),2)
        supLatitud = round(float(input("Ingresa la latitud maxima: ")),2)
        infLongitud = round(float(input("Ingresa la longitud minima: ")),2)
        supLongitud = round(float(input("Ingresa la longitud maxima: ")),2)

        minLatitud = min(infLatitud, supLatitud)
        maxLatitud = max(infLatitud, supLatitud)
        minLongitud = min(infLongitud, supLongitud)
        maxLongitud = max(infLongitud, supLongitud)

        start = tm.process_time()
        
        InRange = controller.getUFOinLocation(catalog, minLatitud, maxLatitud, minLongitud, maxLongitud)

        end = tm.process_time()
        total_time = (end - start)
        
        PrintReq5(InRange, minLatitud, maxLatitud, maxLongitud, minLongitud)
        print("The time it took to execute the requirement was:", total_time*1000 ,"mseg ->",total_time, "seg\n")
        
        if InRange[1] == 0:
            continue 
        print("(Bono) Visualizar los avistamientos de una zona geográfica")
        bono = input("¿Desea ejecutar el bono? (si/no): ").lower()
        if bono == 'si':
            start = tm.process_time()
            controller.getUFOMap(infLatitud, supLongitud, infLongitud, supLatitud)
            end = tm.process_time()
            total_time = (end - start)
            print("The time it took to execute the Bono was:", total_time*1000 ,"mseg ->",total_time, "seg\n")
        else:
            os.remove('Maps\locations.csv')
        
    else:
        sys.exit(0)
        
sys.exit(0)
