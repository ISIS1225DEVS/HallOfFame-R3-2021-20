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
from DISClib.ADT import orderedmap as om
from prettytable import PrettyTable
import prettytable as pt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Crear el catálogo")
    print("2- Cargar información en el catálogo")
    print("3- REQ. 1: Contar los avistamientos en una ciudad")
    print("4- REQ. 2: Contar los avistamientos por duración")
    print("5. REQ. 3: Contar avistamientos por Hora/Minutos del día")
    print("6. REQ. 4: Contar los avistamientos en un rango de fechas")
    print("7. REQ. 5: Contar los avistamientos de una Zona Geográfica")  
    print("8. REQ. 6 (BONO): Visualizar los avistamientos de una zona geográfica")  
    print("0- Salir")

catalog = None
file = 'UFOS//UFOS-utf8-small.csv'


#funciones de impresión
def printFirst5 (catalog):
    lista = lt.subList(catalog['avistamientos'], 1, 5)
    i = 1
    for avista in lt.iterator(lista):
        print(f"{i}. {avista}\n")
        i +=1

def printLast5 (catalog):
    lista = lt.subList(catalog['avistamientos'], lt.size(catalog['avistamientos'])-4, 5)
    i = 1
    for avista in lt.iterator(lista):
        print(f"{i}. {avista}\n")
        i +=1

def printAvistaCity(req1, city):
    table = PrettyTable()
    print(f"{'='*10} Req No. 1 Inputs {'='*10}")
    print(f"UFO Sightings in the city of: {city}",end="\n\n")
    print(f"{'='*10} Req No. 1 Answers {'='*10}")
    print(f"There are {req1[0]} different cities with UFO sightings...")
    print(f"The city with most UFO sightings is: {req1[1][0]} with {req1[1][1]}",end="\n\n")
    print(f"There are {req1[2]} sightings at the: {city} city.")
    if req1[3]:
        print("The first 3 and last 3 UFO sightings in the city are:")
        table.field_names = ["datetime", "city", "state", "country", "shape", "duration (seconds)"]
        table.align = "c"
        table.hrules = pt.ALL
        for i in lt.iterator(req1[4]):
            vals = []
            for j in table.field_names:
                vals.append(i[j])
            table.add_row(vals)
        for i in lt.iterator(req1[5]):
            vals = []
            for j in table.field_names:
                vals.append(i[j])
            table.add_row(vals)
        print(table)

def printCountSightingsDuration(req2,lower,upper):
    tableLongest = PrettyTable()
    print(f"{'='*10} Req No. 2 Inputs {'='*10}")
    print(f"UFO Sightings between {lower} and {upper}",end="\n\n")
    print(f"{'='*10} Req No. 2 Answers {'='*10}")
    print(f"There are {req2[0]} different durations of UFO sightings...")
    print("The longest UFO sighting is:")
    tableLongest.field_names = ["duration (seconds)", "count"]
    tableLongest.hrules = pt.ALL
    tableLongest.add_row([req2[1][0], req2[1][1]])
    print(tableLongest, end="\n\n")
    print(f"There are {req2[2]} sightings between: {lower} and {upper} duration.")
    tablefl3 = PrettyTable()
    tablefl3.hrules = pt.ALL
    tablefl3.field_names = ["datetime", "city", "state", "country", "shape", "duration (seconds)"]
    print("The first 3 and last 3 UFO sightings in the duration time are:")

    for i in lt.iterator(req2[3]):
        vals = []
        for j in tablefl3.field_names:
            vals.append(i[j])
        tablefl3.add_row(vals)

    for i in range(lt.size(req2[4]),0,-1):
        sight = lt.getElement(req2[4],i)
        vals = []
        for j in tablefl3.field_names:
            vals.append(sight[j])
        tablefl3.add_row(vals)        

    print(tablefl3)


def printSightingsByHour(rta, ihour, fhour):
    print("\n"+40*"="+" Req. No. 3 Inputs "+40*"=")
    print(f"UFO sightings between {ihour} and {fhour}")
    print("\n"+40*"="+" Req. No. 3 Answer "+40*"=")
    print(f"The latest UFO sightings time is {rta['latestHour']} with {rta['numLatestSightings']} sightings")
    print(f"\nThere are {rta['numSightings']} sightings between {ihour} and {fhour}")
    print("The first 3 and last 3 UFO sightings in this time are:")
    print("\nFirst 3:")
    j = 1
    for i in lt.iterator(rta["first3"]):
        print(f"{j}. {i}\n")
        j += 1
    print("\nLast 3:")
    j = 1
    for i in lt.iterator(rta["last3"]):
        print(f"{j}. {i}\n")
        j += 1



def printCountSightingsDateRange(req4, lowDate, upDate):
    tableOldest = PrettyTable()
    print(f"{'='*10} Req No. 4 Inputs {'='*10}")
    print(f"UFO Sightings between {lowDate} and {upDate}",end="\n\n")
    print(f"{'='*10} Req No. 4 Answers {'='*10}")
    print(f"There are {req4[0]} UFO sightings with different dates [YYYY-MM-DD]...")
    print("The oldest UFO sighting is:")
    tableOldest.field_names = ["date", "count"]
    tableOldest.hrules = pt.ALL
    tableOldest.add_row([req4[1][0], req4[1][1]])
    print(tableOldest, end="\n\n")
    print(f"There are {req4[2]} sightings between: {lowDate} and {upDate} duration.")
    tablefl3 = PrettyTable()
    tablefl3.hrules = pt.ALL
    tablefl3.field_names = ["datetime","date","city", "state", "country", "shape", "duration (seconds)"]
    print("The first 3 and last 3 UFO sightings in this time are:")

    for i in lt.iterator(req4[3]):
        vals = []
        for j in tablefl3.field_names:
            vals.append(i[j])
        tablefl3.add_row(vals)

    for i in range(lt.size(req4[4]),0,-1):
        sight = lt.getElement(req4[4],i)
        vals = []
        for j in tablefl3.field_names:
            vals.append(sight[j])
        tablefl3.add_row(vals)        

    print(tablefl3)

def printCountSightingsZone(req5, latmin, latmax, longmin, longmax,req):
    print(f"{'='*10} Req No. {req} Inputs {'='*10}")
    print(f"UFO Sightings between latitude range of {latmin} and {latmax}")
    print(f" plus longitude range of {longmin} and {longmax}")
    print(f"{'='*10} Req No. {req} Answers {'='*10}")
    print(f"There are {req5[0]} different UFO sightings in the current area")
    tablefl5 = PrettyTable()
    tablefl5.hrules = pt.ALL
    tablefl5.field_names = ["datetime","city", "state", "country", "shape", "duration (seconds)", "latitude", "longitude"]
    print("The first 5 and last 5 UFO sightings in this area are:")
    if req5[1]:
        for i in lt.iterator(req5[2]):
            vals = []
            for j in tablefl5.field_names:
                vals.append(i[j])
            tablefl5.add_row(vals)
        for i in lt.iterator(req5[3]):
            vals = []
            for j in tablefl5.field_names:
                vals.append(i[j])
            tablefl5.add_row(vals)    
    else:
        for i in lt.iterator(req5[2]):
            vals = []
            for j in tablefl5.field_names:
                vals.append(i[j])
            tablefl5.add_row(vals)
    print(tablefl5)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nCreando el catálogo ....\n")
        catalog = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos ....")
        controller.loadData(catalog, file)
        print("\nAvistamientos cargados: "+ str(lt.size(catalog['avistamientos'])))
        print("\nPrimeros 5 avistamientos: \n")
        printFirst5(catalog)
        print("\nÚltimos 5 avistamientos: \n")
        printLast5(catalog)
        print("")
    
    elif  int(inputs[0]) == 3:
        city = input("\nIngrese el nombre de la ciudad a consultar: ")
        req1 = controller.countSightingsCity(catalog, city)
        if req1:
            print(len(req1))
            printAvistaCity(req1, city)
        else:
            print("No ingreso una ciudad validad intente nuevamente")
    
    elif int(inputs[0]) == 4:
        try:
            lower = float(input("Ingrese la duración en segundos minima (puede tener decimales): "))
            upper = float(input("Ingrese la duración en segundos maxima (puede tener decimales): "))
            if lower <= upper:
                req2 = controller.countSightingsDuration(catalog, lower, upper)
                printCountSightingsDuration(req2,lower,upper)
            else:
                print("lower debe ser menor que upper")
        except:
            print("Los valores deben ser numeros")

    elif int(inputs[0]) == 5:
        ihour = input("Ingrese hora mínima del día (HH:MM): ")
        fhour = input("Ingrese hora máxima del día (HH:MM): ")
        try:
            req3 = controller.sightingsByHour(catalog, ihour, fhour)
            printSightingsByHour(req3, ihour, fhour)
        except:
            print("\nEn rango de horas no es válido\n")
    

    elif int(inputs[0]) == 6:
        lowDate = input("Ingrese la fecha minima (AAAA-MM-DD): ")
        upDate = input("Ingrese la fecha maxima (AAAA-MM-DD): ")
        try:
            req4 = controller.countSightingsDateRange(catalog, lowDate, upDate)
            printCountSightingsDateRange(req4, lowDate, upDate)
        except:
            print("Las fechas ingresadas no son validas")

    elif int(inputs[0]) == 7:
        latmin = float(input("Ingrese la latitud minima: "))
        latmax = float(input("Ingrese la latitud maxima: "))
        longmin = float(input("Ingrese la longitud minima: "))
        longmax = float(input("Ingrese la longitud maxima: "))
        req5 = controller.countSightingsZone(catalog, latmin, latmax, longmin, longmax)
        printCountSightingsZone(req5, latmin, latmax, longmin, longmax,5)

    elif int(inputs[0]) == 8:
        latmin = float(input("Ingrese la latitud minima: "))
        latmax = float(input("Ingrese la latitud maxima: "))
        longmin = float(input("Ingrese la longitud minima: "))
        longmax = float(input("Ingrese la longitud maxima: "))
        req6 = controller.createMapReq5(catalog, latmin, latmax, longmin, longmax)
        printCountSightingsZone(req6,latmin,latmax,longmin,longmax,6)
        
    
    else:
        sys.exit(0)
sys.exit(0)
