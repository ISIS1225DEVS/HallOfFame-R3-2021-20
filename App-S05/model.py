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
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import mergesort as mer
import datetime
assert cf
import folium
import webbrowser
import pandas as pd
import csv
import os

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de avistamientos de UFOS
    """

    catalog = {}

    catalog['Ufos'] = lt.newList('ARRAY_LIST')

    catalog['cityIndex'] = om.newMap(omaptype='RBT',
                                     comparefunction=compareString)

    catalog['durationIndex'] = om.newMap(omaptype='RBT',
                                     comparefunction=compareFloat)
                        
    catalog['timeIndex'] = om.newMap(omaptype='RBT',
                                     comparefunction=compareTime)
                                    
    catalog['dateIndex'] = om.newMap(omaptype='RBT',
                                     comparefunction=compareTime)

    catalog['latitudeIndex'] = om.newMap(omaptype='RBT',
                                     comparefunction=compareFloat)

    return catalog
    
# Funciones para agregar informacion al catalogo

def addUFO(catalog, ufo):
    """
    Agrega un avistamiento de UFO al catálogo
    """
    info = {}
    info['datetime'] = datetime.datetime.strptime(ufo['datetime'], '%Y-%m-%d %H:%M:%S')
    info['city'] = ufo['city']
    info['state'] = ufo['state']
    info['country'] = ufo['country']
    info['shape'] = ufo['shape']
    info['duration (seconds)'] = float(ufo['duration (seconds)'])
    info['duration (hours/min)'] = ufo['duration (hours/min)']
    info['comments'] = ufo['comments']
    info['date posted'] = datetime.datetime.strptime(ufo['date posted'], '%Y-%m-%d %H:%M:%S')
    info['latitude'] = float(ufo['latitude'])
    info['longitude'] = float(ufo['longitude'])

    for key in info:
        if info[key] == "":
            info[key] = "unknown"

    lt.addLast(catalog['Ufos'], info)
    updateCityIndex(catalog['cityIndex'], info)
    updateDurationIndex(catalog['durationIndex'], info)
    updateTimeIndex(catalog['timeIndex'], info)
    updateDateIndex(catalog['dateIndex'], info)
    updatelatitudeIndex(catalog['latitudeIndex'], info)

def updateCityIndex (mapa, ufo):
    """
    Se toma la ciudad del avistamiento y se busca si ya existe 
    en el arbol dicha ciudad. 

    -Si se encuentra, se adiciona a su lista de avistamientos.
    -Si no se encuentra, crea un nodo para esa ciudad en el
     arbol.
    """
    ufocity = ufo['city'].lower()
    entry = om.get(mapa, ufocity)
    if entry is None:
        cityentry = newCity(ufocity)
        om.put(mapa, ufocity, cityentry)
    else:
        cityentry = me.getValue(entry)

    lt.addLast(cityentry['ufos'], ufo)
    cityentry['size']+=1

def updateDurationIndex (mapa, ufo):
    """
    Se toma la duracion del avistamiento y se busca si ya existe 
    en el arbol dicha duracion. 

    -Si se encuentra, se adiciona a su lista de avistamientos.
    -Si no se encuentra, crea un nodo para esa duracion en el
     arbol.
    """
    ufoduration = ufo['duration (seconds)']
    entry = om.get(mapa, ufoduration)
    if entry is None:
        durationentry = newDuration(ufoduration)
        om.put(mapa, ufoduration, durationentry)
    else:
        durationentry = me.getValue(entry)

    lt.addLast(durationentry['ufos'], ufo)
    durationentry['size']+=1

def updateTimeIndex (mapa, ufo):
    """
    Se toma la hora [HH:MM] del avistamiento y se busca si ya 
    existe en el arbol dicha hora. 

    -Si se encuentra, se adiciona a su lista de avistamientos.
    -Si no se encuentra, crea un nodo para esa hora en el
     arbol.
    """
    ufotime = ufo['datetime'].time()
    entry = om.get(mapa, ufotime)
    if entry is None:
        timeentry = newTime(ufotime)
        om.put(mapa, ufotime, timeentry)
    else:
        timeentry = me.getValue(entry)

    lt.addLast(timeentry['ufos'], ufo)
    timeentry['size'] += 1

def updateDateIndex (mapa, ufo):
    """
    Se toma la fecha [AAAA-MM-DD] del avistamiento y se busca 
    si ya existe en el arbol dicha fecha. 

    -Si se encuentra, se adiciona a su lista de avistamientos.
    -Si no se encuentra, crea un nodo para esa fecha en el
     arbol.
    """
    ufodate = ufo['datetime'].date()
    entry = om.get(mapa, ufodate)
    if entry is None:
        dateentry = newDate(ufodate)
        om.put(mapa, ufodate, dateentry)
    else:
        dateentry = me.getValue(entry)

    lt.addLast(dateentry['ufos'], ufo)
    dateentry['size'] += 1

def updatelatitudeIndex (mapa, ufo):
    """
    Se toma la latitud del avistamiento y se busca si ya 
    existe en el arbol dicha latitud. 

    -Si se encuentra, se adiciona a su lista de avistamientos y 
     se actualiza el indice de longitud.
    -Si no se encuentra, crea un nodo para esa latitud en el
     arbol.
    """
    ufolatitud = round(ufo['latitude'],2)
    entry = om.get(mapa, ufolatitud)
    if entry is None:
        latitudentry = newlatitude(ufolatitud)
        om.put(mapa, ufolatitud, latitudentry)
    else:
        latitudentry = me.getValue(entry)

    latitudentry['size'] += 1
    updatelongitudeIndex(latitudentry['longitude'], ufo)

def updatelongitudeIndex (mapa, ufo):
    """
    Se toma la longitud del avistamiento y se busca si ya 
    existe en el arbol dicha longitud. 

    -Si se encuentra, se adiciona a su lista de avistamientos.
    -Si no se encuentra, crea un nodo para esa longitud en el
     arbol.
    """
    ufolongitud = round(ufo['longitude'],2)
    entry = om.get(mapa, ufolongitud)
    if entry is None:
        longitudentry = newlongitude(ufolongitud)
        om.put(mapa, ufolongitud, longitudentry)
    else:
        longitudentry = me.getValue(entry)

    lt.addLast(longitudentry['ufos'], ufo)
    longitudentry['size'] += 1

# Funciones para creacion de datos

def newCity(city):
    """
    Crea una entrada en el indice por ciudad, es decir en el arbol
    binario.
    """
    entry = {'city': None, 'ufos': None, 'size':0}
    entry['city'] = city
    entry['ufos'] = lt.newList('ARRAY_LIST')
    return entry
    
def newDuration(duration):
    """
    Crea una entrada en el indice por duracion, es decir en el arbol
    binario.
    """
    entry = {'duration': None, 'ufos': None, 'size':0}
    entry['duration'] = duration
    entry['ufos'] = lt.newList('ARRAY_LIST')
    return entry

def newTime(time):
    """
    Crea una entrada en el indice por hora, es decir en el arbol
    binario.
    """
    entry = {'time': None, 'ufos': None, 'size':0}
    entry['time'] = time
    entry['ufos'] = lt.newList('ARRAY_LIST')
    return entry

def newDate(date):
    """
    Crea una entrada en el indice por fecha, es decir en el arbol
    binario.
    """
    entry = {'date': None, 'ufos': None, 'size':0}
    entry['date'] = date
    entry['ufos'] = lt.newList('ARRAY_LIST')
    return entry

def newlatitude(latitud):
    """
    Crea una entrada en el indice por latitud, es decir en el arbol
    binario.
    """
    entry = {'latitude': None, 'longitude':None, 'size':0}
    entry['latitude'] = latitud
    entry['longitude'] = om.newMap(omaptype='RBT',
                                  comparefunction=compareFloat)
    return entry

def newlongitude(longitud):
    """
    Crea una entrada en el indice por longitud, es decir en el arbol
    binario.
    """
    entry = {'longitude': None,'ufos': None, 'size':0}
    entry['longitude'] = longitud
    entry['ufos'] = lt.newList('ARRAY_LIST')
    return entry

# Funciones de consulta

def getFirst(lista, num):
    """
    Retorna los primeros num elementos de una lista
    """
    lista = lt.subList(lista, 1, num)
    return lista

def getLast(lista, num):
    """
    Retorna los ultimos num elementos de una lista
    """
    lista = lt.subList(lista, lt.size(lista)-(num-1), num)
    return lista

def FirtsAndLast(primeros, ultimos):
    for item in lt.iterator(ultimos):
        lt.addLast(primeros, item)
    return primeros


def UfosSize(catalog):
    """
    Número de avistamientos totales
    """
    return lt.size(catalog['Ufos'])


def indexHeight(catalog, indice):
    """
    Altura del arbol
    """
    return om.height(catalog[indice])

def indexSize(catalog, indice):
    """
    Número de elementos en el indice
    """
    return om.size(catalog[indice])

#Requerimientos

def getUFOTopCity(catalog):
    """
    Req 1: Retorna el Top 5 ciudades con mas avistamientos

    Complejidad:
    n = numero de elementos en el RBT de ciudades
    log2(n) = altura del RBT de ciudades
    
    O(log2(n) + n + n*log2(n))
    """
    keys = om.keySet(catalog['cityIndex']) #O(log2(n))
    topCity = None
    topCount = 0
    for key in lt.iterator(keys): #O(n)
        entry = om.get(catalog['cityIndex'], key) #O(n*log2(n))
        value = me.getValue(entry)
        
        if value['size'] > topCount:
            topCount = value['size']
            topCity = value['city']

    return topCity, topCount, lt.size(keys)

def getUFOByCity(catalog, city):
    """
    Req 1:
    Busca la ciudad que ingresa por parametro en el cityIndex (ciudad, lista Ufos)

    param:
        -catalog: Catalgo de Ufos
        -city: Nombre de la ciudad a consultar
    return:
        -None: Si no se encontro el la ciudad
        -tuple:
            -List: Lista de avistamientos en la ciudad
            -Int: El numero total de avistamientos en la ciudad
        
    Complejidad:
    n = numero de elementos en el RBT de ciudades
    log2(n) = altura del RBT de ciudades
    
    O(log2(n))
    """
    entry = om.get(catalog['cityIndex'], city) #O(log2(n))
    if not entry:
        return None
    value = me.getValue(entry)
    ltUfos = value['ufos']
    size = value['size']
    return ltUfos, size
    

def getUFOTopDuration(catalog):
    """
    Req 2 Retorna el Top 5 duraciones mas largas

    Complejidad:
    n = numero de elementos en el RBT de duracion
    log2(n) = altura del RBT de duracion
    
    O(log2(n) + log2(n)) → O(log2(n))
    """
    mapa = catalog['durationIndex']
    size = om.size(mapa)
    top = om.get(mapa,om.maxKey(mapa))['value']
    return top, size

def getUFOByDuration(catalog, minimo, maximo):
    """
    Req 2:
    Busca la los avistamientos en el rango dado, con el metodo values(),
    Agrega a una lista los avistamientos que se encuentran en el rango
    de duracion dado.

    param:
        -catalog: Catalgo de Ufos
        -minimo: Duración minima
        -maximo: Duración maxima
    return:
        -tuple:
            -List: Lista de avistamientos en el rango de duracion dado
            -Int: El numero total de avistamientos en el rango de duracion dado

    Complejidad: 
    n = numero de elementos en el RBT de ciudades
    log2(n) = altura del RBT de duracion
    #llaves = numero de llaves en el rango dado
    #avistamientos = numero de avistamientos en en rango de duracion dado

    O(log2(n) + #llaves + #llaves + #avistamientos) → O(log2(n) + #llaves + #avistamientos)
    """
    ltUfos = lt.newList('ARRAY_LIST')
    values = om.values(catalog['durationIndex'], minimo, maximo)
    for value in lt.iterator(values):
        for ufo in lt.iterator(value['ufos']):
            lt.addLast(ltUfos, ufo)
    return ltUfos, lt.size(ltUfos)

def getTopTime(catalog):
    """
    Req 3: Retorna el Top 5 horas [HH:MM] mas tardias

    Complejidad: 
    n = numero de elementos en el RBT de ciudades
    log2(n) = altura del RBT de tiempo
    
    O(log2(n) + log2(n)) → O(log2(n))
    """
    mapa = catalog['timeIndex']
    size = om.size(mapa) 
    top = om.get(mapa,om.maxKey(mapa))['value'] #O(log2(n) + log2(n))
    return top, size

def getUFOinTime(catalog, inf, sup):
    """
    Req 3:
    Busca la los avistamientos en el rango dado, con el metodo values(),
    Agrega a una lista los avistamientos que se encuentran en el rango
    de tiempo dado.

    param:
        -catalog: Catalgo de Ufos
        -inf: Hora [HH:MM] minima
        -sup: Hora [HH:MM] maxima
    return:
        -tuple:
            -List: Lista de avistamientos en el rango de tiempo dado
            -Int: El numero total de avistamientos en el rango de tiempo dado
    
    Complejidad: 
    n = numero de elementos en el RBT de ciudades
    log2(n) = altura del RBT de tiempo
    #llaves = numero de llaves en el rango dado
    #avistamientos = numero de avistamientos en en rango de tiempo dado

    O(log2(n) + #llaves + #llaves + #avistamientos) → O(log2(n) + #llaves + #avistamientos)
    """
    values = om.values(catalog['timeIndex'], inf, sup) #O(log2(n) + #llaves)
    ltUfos = lt.newList('ARRAY_LIST')
    for value in lt.iterator(values): #O(#llaves)
        for ufo in lt.iterator(value['ufos']): #O(#avistamientos)
            lt.addLast(ltUfos, ufo)
    return ltUfos, lt.size(ltUfos)

def getUFOinDate(catalog, inf, sup):
    """
    Req 4:
    Busca la los avistamientos en el rango dado, con el metodo values(),
    Agrega a una lista los avistamientos que se encuentran en el rango
    de fechas dado.

    param:
        -catalog: Catalgo de Ufos
        -inf: Fecha [AAAA-MM-DD] minima
        -sup: Fecha [AAAA-MM-DD] maxima
    return:
        -tuple:
            -List: Lista de avistamientos en el rango de fechas dado
            -Int: El numero total de avistamientos en el rango de fechas 
    
    Complejidad: 
    n = numero de elementos en el RBT de ciudades
    log2(n) = altura del RBT de fecha
    #llaves = numero de llaves en el rango dado
    #avistamientos = numero de avistamientos en en rango de fechas dado

    O(log2(n) + #llaves + #llaves + #avistamientos) → O(log2(n) + #llaves + #avistamientos)
    """
    values = om.values(catalog['dateIndex'], inf, sup) #O(log2(n) + #llaves)
    ltUfos = lt.newList('ARRAY_LIST')
    for value in lt.iterator(values): #O(#llaves)
        for ufo in lt.iterator(value['ufos']): #O(#avistamientos)
            lt.addLast(ltUfos, ufo)

    return ltUfos, lt.size(ltUfos)

def getTopDate(catalog):
    """
    Req 4: Retorna el Top 5 fechas [AAAA-MM-DD] mas antiguas

    Complejidad:
    n = numero de elementos en el RBT de ciudades
    log2(n) = altura del RBT de fecha

    O(log2(n) + log2(n)) → O(log2(n))
    """
    mapa = catalog['dateIndex']
    size = om.size(mapa)
    top = om.get(mapa, om.minKey(mapa))['value'] #O(log2(n) + log2(n))
    return top, size

def getUFOinLocation(catalog, minLatitud, maxLatitud, minLongitud, maxLongitud): #no estoy segura de la complejidad :(
    """
    Req 5:
    Busca la los avistamientos en el rango dado, con el metodo values(),
    Agrega a una lista los avistamientos que se encuentran en el rango
    de latitud y longitud dado.

    param:
        -catalog: Catalgo de Ufos
        -minLatitud: Latitud minima
        -maxLatitud: Latitud maxima
        -minLongitud: Longitud minima
        -maxLongitud: Longitud maxima
    return:
        -tuple:
            -List: Lista de avistamientos en el rango de latitud y longitud dado
            -Int: El numero total de avistamientos en el rango de latitud y longitud dado

    Complejidad: 
    log2(a) = altura del RBT de latitud
    log2(o) = altura promedio de todos los RBT que se recorren de longitud
    #llaves-a = numero de llaves en el rango de latitud dado 
    #llaves-o = numero de llaves en el rango de longitud-latitud dado
    #avistamientos = numero de avistamientos en en rango de latitud y longitud dado

    O(#avistamientos + log2(a)+ #llaves-a)
    """
    mapa = catalog['latitudeIndex']
    ltUfos = lt.newList('ARRAY_LIST')
    rangeLatitud = om.values(mapa,minLatitud,maxLatitud)# O(log2(a) + #llaves-a)

    for latitud in lt.iterator(rangeLatitud):# O(#llaves-a)
        rangeLongitud = om.values(latitud['longitude'], minLongitud, maxLongitud)# O(log(o) + #llaves-o)
        for longitud in lt.iterator(rangeLongitud):# O(#llaves-o)
            for ufo in lt.iterator(longitud['ufos']):# O(#avistamientos)
                lt.addLast(ltUfos, ufo)

    return ltUfos, lt.size(ltUfos)

def getUFOMap(infLatitud, supLongitud, infLongitud, supLatitud): #ni idea de la complejidad :(
    """
    Req 6 (Bono)
    """
    mapa = folium.Map(location = [infLatitud, supLongitud],
                    min_lot=infLongitud,
                    max_lot=supLongitud,
                    min_lat=infLatitud,
                    max_lat=supLatitud)

    df = pd.read_csv('Maps\locations.csv')
    tooltip = "Click me!"
    df.apply(lambda row:folium.Marker(location=[row["Latitude"], row["Longitude"]], 
            radius=10,Tooltip=tooltip, popup=folium.Popup('City: ' + row['City'] + '<br>' + 'Datetime: ' + row['Datetime'], 
            min_width=200, max_width=200), icon=folium.Icon(color='green')).add_to(mapa), axis=1)

    mapa.save("Maps\map.html")
    webbrowser.open('Maps\map.html')
    os.remove("Maps\locations.csv")


# Funciones utilizadas para comparar elementos dentro de una lista

def compareDates(date1, date2):
    """
    Compara dos tipos de fecha
    """
    date = me.getKey(date2)
    if (date1 == date):
        return 0
    elif (date1 > date):
        return 1
    else:
        return -1

def compareString(str1, str2):
    """
    Compara dos strings
    """
    if (str1.lower() == str2.lower()):
        return 0
    elif (str1.lower() > str2.lower()):
        return 1
    else:
        return -1

def compareFloat(num1, num2):
    """
    Compara dos Floats
    """
    num1 = float(num1)
    num2 = float(num2)
    if (num1 == num2):
        return 0
    elif (num1 > num2):
        return 1
    else:
        return -1
    
def compareTime (time1, time2):
    """
    Compara dos Fechas
    """
    if (time1 == time2):
        return 0
    elif (time1 > time2):
        return 1
    else:
        return -1

def cmpByCount (city1, city2):
    return city1['count'] > city2['count']

def cmpDuration(ufo1, ufo2):
    return ufo1['duration'] > ufo2['duration']

def cmpDate (ufo1, ufo2):
    return ufo1['datetime'] < ufo2['datetime']

def cmpCountry (ufo1, ufo2):
    return ufo1['country'] < ufo2['country']

def cmpCity (ufo1, ufo2):
    return ufo1['city'] < ufo2['city']

# Funciones de ordenamiento

def SortData(catalog):
    cityIndex = om.valueSet(catalog['cityIndex'])
    durationIndex = om.valueSet(catalog['durationIndex'])
    timeIndex = om.valueSet(catalog['timeIndex'])
    dateIndex = om.valueSet(catalog['dateIndex'])

    for city in lt.iterator(cityIndex):
        mer.sort(city['ufos'], cmpDate) #Ordenarlo por fecha y hora

    for duration in lt.iterator(durationIndex):
        mer.sort(duration['ufos'], cmpCountry) #ordenar por pais
        mer.sort(duration['ufos'], cmpCity) #ordenar por ciudad
        
        
    for time in lt.iterator(timeIndex):
        mer.sort(time['ufos'], cmpDate) #Ordenarlo por fecha

    for date in lt.iterator(dateIndex):
        mer.sort(date['ufos'], cmpDate)
