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
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.ADT import orderedmap as om
from datetime import datetime as dt
import folium
assert cf


# Construccion de modelos
def newCatalog():
    catalog = {'avistamientos': None,
                'city': None}
    catalog['avistamientos'] = lt.newList('ARRAY_LIST')
    catalog['city'] = om.newMap('RBT')
    catalog["duration"] = om.newMap("RBT")
    catalog["Date"] = om.newMap("RBT")
    catalog["latitude"] = om.newMap("RBT")
    catalog["hour"] = om.newMap("RBT")


    
    return catalog
    

# Funciones para agregar informacion al catalogo

def addAvist(catalog, avist):
    avist = formatAvist(avist)
    lt.addLast(catalog['avistamientos'], avist)
    
    #llenar el arbol con llave ciudad
    if om.contains(catalog['city'], avist['city']):
        lt.addLast(me.getValue(om.get(catalog['city'], avist['city'])), avist)
    else:
        om.put(catalog['city'], avist['city'], lt.newList("ARRAY_LIST"))
        lt.addLast(me.getValue(om.get(catalog['city'], avist['city'])),avist)
    
    #llenar el arbol con llave duración
    if om.contains(catalog['duration'], avist['duration (seconds)']):
        lt.addLast(me.getValue(om.get(catalog['duration'], avist['duration (seconds)'])), avist)
    else:
        om.put(catalog['duration'], avist['duration (seconds)'], lt.newList("ARRAY_LIST"))
        lt.addLast(me.getValue(om.get(catalog['duration'], avist['duration (seconds)'])),avist)

    #llenar el arbol con llave fecha
    if om.contains(catalog["Date"], avist["datetime"].date()):
        lt.addLast(me.getValue(om.get(catalog["Date"], avist["datetime"].date())), avist)
    else:
        om.put(catalog['Date'], avist['datetime'].date(), lt.newList("ARRAY_LIST"))
        lt.addLast(me.getValue(om.get(catalog['Date'], avist['datetime'].date())),avist)

    #llenar arbol con llave hora
    if om.contains(catalog["hour"], avist["datetime"].time()):
        lt.addLast(me.getValue(om.get(catalog["hour"], avist["datetime"].time())), avist)
    else:
        om.put(catalog['hour'], avist['datetime'].time(), lt.newList("ARRAY_LIST"))
        lt.addLast(me.getValue(om.get(catalog['hour'], avist['datetime'].time())),avist)



    #llenar el arbol con llave latitude
    roundLong = round(avist["longitude"],2)
    roundLat = round(avist["latitude"],2)
    if om.contains(catalog["latitude"], roundLat):
        arbolLong = me.getValue(om.get(catalog["latitude"], roundLat))
        if om.contains(arbolLong, roundLong):
            lt.addLast(me.getValue(om.get(arbolLong, roundLong)), avist)
        else:
            om.put(arbolLong, roundLong, lt.newList("ARRAY_LIST"))
            lt.addLast(me.getValue(om.get(arbolLong, roundLong)), avist)
    else:
        om.put(catalog["latitude"], roundLat, om.newMap())
        arbolLong = me.getValue(om.get(catalog["latitude"], roundLat))
        if om.contains(arbolLong, roundLong):
            lt.addLast(me.getValue(om.get(arbolLong, roundLong)), avist)
        else:
            om.put(arbolLong, roundLong, lt.newList("ARRAY_LIST"))
            lt.addLast(me.getValue(om.get(arbolLong, roundLong)), avist)


#Funciones formato datos
def formatAvist(avist):
    avist["duration (seconds)"] = float(avist["duration (seconds)"])
    avist["latitude"] = float(avist["latitude"])
    avist["longitude"] = float(avist["longitude"])
    avist["datetime"] = dt.strptime(avist["datetime"], "%Y-%m-%d %H:%M:%S")
    return avist

# Funciones para creacion de datos

# Funciones de consulta

#Requerimiento 1
def countSightingsCity(catalog, city):
    totalCiudades = om.size(catalog["city"])

    all = lt.newList("ARRAY_LIST")
    keyValueSet(catalog["city"]["root"], all)
    key = None
    most = 0
    for i in lt.iterator(all):
        if i[1] > most:
            key = i[0]
            most = i[1]

    if om.contains(catalog["city"], city):
        vals = om.get(catalog["city"], city)
        numCity = lt.size(me.getValue(vals))
        ordered = ms.sort(me.getValue(vals), lambda x,y: x["datetime"] < y["datetime"])
        if lt.size(ordered) < 6:
            return (totalCiudades, (key,most), numCity, False, ordered)
        else:
            first3 = lt.subList(ordered,1,3)
            last3 = lt.subList(ordered, lt.size(ordered)-2,3)
            return (totalCiudades, (key,most), numCity, True, first3, last3)
    else:
        return False





#Requerimiento 2
def countSightingsDuration(catalog, lower, upper):
    dur = catalog["duration"]
    numDifs = om.size(dur)
    maxDur = om.maxKey(dur)
    countMax = lt.size(me.getValue(om.get(dur, maxDur)))
    vals = lt.newList("ARRAY_LIST")
    vals = valuesRange(dur["root"],lower,upper,vals, dur["cmpfunction"])
    numSights = size(vals)
    first3 = lt.newList("ARRAY_LIST")
    last3 = lt.newList("ARRAY_LIST")


    for i in range(1,lt.size(vals)+1):
        data = lt.getElement(vals, i)
        for j in lt.iterator(data):
            if lt.size(first3) < 3:
                lt.addLast(first3, j)
            else:
                break
        if lt.size(first3) == 3:
            break

    for i in range(lt.size(vals),0,-1):
        data = lt.getElement(vals, i)
        for j in range(lt.size(data),0,-1):
            sighting = lt.getElement(data,j)
            if lt.size(last3) < 3:
                lt.addLast(last3, sighting)
            else:
                break
        if lt.size(last3) == 3:
            break
    
    return (numDifs, (maxDur, countMax), numSights, first3, last3)


#Requerimiento 3
def sightingsByHour(catalog, ihour, fhour):
    ihour = dt.strptime(ihour, "%H:%M").time()
    fhour = dt.strptime(fhour, "%H:%M").time()
    rta = {}
    maxKey = om.maxKey(catalog["hour"])
    rta["latestHour"] = maxKey
    rta["numLatestSightings"] = lt.size(me.getValue(om.get(catalog["hour"], maxKey)))
    listaSightingsByHour = om.values(catalog["hour"], ihour, fhour)
    lista = lt.newList("ARRAY_LIST")
    for i in lt.iterator(listaSightingsByHour):
        for j in lt.iterator(i):
            dicc = {"Fecha": dt.strftime(j["datetime"],"%Y-%m-%d" ), "Hora": dt.strftime(j["datetime"], "%H:%M"),
             "Ciudad": j["city"], "País": j["country"], "Duración (s)": j["duration (seconds)"], "Forma": j["shape"]}
            lt.addLast(lista, dicc)
    rta["numSightings"] = lt.size(lista)
    ms.sort(lista, cmpSightingsreq3)
    rta["first3"] = lt.subList(lista, 1, 3)
    rta["last3"] = lt.subList(lista, lt.size(lista)-2, 3)
    return rta



#Requerimiento 4
def countSightingsDateRange(catalog, lowDate, upDate):
    lowDate = dt.fromisoformat(lowDate).date()
    upDate = dt.fromisoformat(upDate).date()
    dateMap = catalog["Date"]
    numSights = om.size(dateMap)
    minDate = om.minKey(dateMap)
    countMin = lt.size(me.getValue(om.get(dateMap,minDate)))
    vals = lt.newList("ARRAY_LIST")
    vals = valuesRange(dateMap["root"],lowDate, upDate,vals, dateMap["cmpfunction"])
    numinRange = size(vals)
    first3 = lt.newList("ARRAY_LIST")
    last3 = lt.newList("ARRAY_LIST")


    for i in range(1,lt.size(vals)+1):
        data = lt.getElement(vals, i)
        for j in lt.iterator(data):
            if lt.size(first3) < 3:
                j["date"] = j["datetime"].date()
                lt.addLast(first3, j)
            else:
                break
        if lt.size(first3) == 3:
            break

    for i in range(lt.size(vals),0,-1):
        data = lt.getElement(vals, i)
        for j in range(lt.size(data),0,-1):
            sighting = lt.getElement(data,j)
            if lt.size(last3) < 3:
                sighting["date"] = sighting["datetime"].date()
                lt.addLast(last3, sighting)
            else:
                break
        if lt.size(last3) == 3:
                break
    return (numSights, (minDate, countMin), numinRange, first3, last3)




#Requerimiento 5
def countSightingsZone(catalog, latmin, latmax, longmin, longmax):
    treeLat = catalog["latitude"]
    valsLat = lt.newList("ARRAY_LIST")
    valsLat = valuesRange(treeLat["root"], latmin, latmax, valsLat, treeLat["cmpfunction"])
    result = lt.newList("ARRAY_LIST")
    for treeLong in lt.iterator(valsLat):
        valsLong = lt.newList("ARRAY_LIST")
        valsLong = valuesRange(treeLong["root"], longmin, longmax , valsLong, treeLong["cmpfunction"])
        if lt.size(valsLong) > 0:
            for listLongLat in lt.iterator(valsLong):
                for sighting in lt.iterator(listLongLat):
                    lt.addLast(result, sighting)

    numSights = lt.size(result)
    if numSights >= 10:
        first5 = lt.subList(result,1,5)
        last5 = lt.subList(result, numSights-4, 5)
        return (numSights, True, first5, last5)
    else:
        return numSights, False ,result

def createMapReq5(catalog, latmin, latmax, longmin, longmax):
    req5 = countSightingsZone(catalog,latmin,latmax, longmin, longmax)
    centroide = ((latmin+latmax)/2, (longmax+longmin)/2)

    mapa = folium.Map(location=centroide, zoom_start=6)
    folium.Rectangle(bounds=[(latmin,longmin), (latmax, longmax)], fill=True).add_to(mapa)
    table = lambda i: """<style>
                            table,
                            th,
                            td {
                                padding: 10px;
                                border: 1px solid black;
                                border-collapse: collapse;
                                }
                            </style>"""+f""" <table> 
                                <tr> 
                                    <th>City</th>
                                    <th>Datetime</th>
                                    <th>Duration [s]</th>
                                    <th>Shape</th>
                                    <th>Comments</th>
                                </tr>
                                <tr>
                                    <td>{i["city"]}</td>
                                    <td>{i["datetime"]}</td>
                                    <td>{i["duration (seconds)"]}</td>
                                    <td>{i["shape"]}</td>
                                    <td>{i["comments"]}</td> 
                                </tr>
                            </table>"""

    if req5[1]:
        for i in lt.iterator(req5[2]):
            folium.Marker(
                (i["latitude"], i["longitude"]),
                icon=folium.Icon(icon="reddit-alien", prefix="fa",color="blue"),
                tooltip = f"{i['city'].title()}",
                popup= table(i)

            ).add_to(mapa)
        for i in lt.iterator(req5[3]):
            folium.Marker(
                (i["latitude"], i["longitude"]),
                icon=folium.Icon(icon="reddit-alien", prefix="fa",color="blue"),
                tooltip = f"{i['city'].title()}",
                popup= table(i)

            ).add_to(mapa)
    else:
        for i in lt.iterator(req5[2]):
            folium.Marker(
                (i["latitude"], i["longitude"]),
                icon=folium.Icon(icon="reddit-alien", prefix="fa",color="blue"),
                tooltip = f"{i['city'].title()}",
                popup= table(i)

            ).add_to(mapa)
    mapa.save("mapa.html")
    return req5

#Funciones de ayuda
def keyValueSet(root, klist):
    if root is not None:
        keyValueSet(root['left'], klist)
        lt.addLast(klist, (root["key"],lt.size(root['value'])))
        keyValueSet(root['right'], klist)

def size(vlist):
    suma = 0
    for i in lt.iterator(vlist):
        suma += lt.size(i)

    return suma


def valuesRange(root, keylo, keyhi, lstvalues, cmpfunction):
        if (root is not None):
            complo = cmpfunction(keylo, root['key'])
            comphi = cmpfunction(keyhi, root['key'])

            if (complo < 0):
                valuesRange(root['left'], keylo, keyhi, lstvalues,
                            cmpfunction)
            if ((complo <= 0) and (comphi >= 0)):
                lt.addLast(lstvalues, root['value'])
            if (comphi > 0):
                valuesRange(root['right'], keylo, keyhi, lstvalues,
                            cmpfunction)
        return lstvalues

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpSightingsreq3 (sighting1, sighting2):
    if sighting1["Hora"] < sighting2["Hora"]:
        return True
    elif sighting1["Hora"] == sighting2["Hora"]:
        if sighting1["Fecha"] < sighting2["Fecha"]:
            return True
        else:
            return False
    else:
        return False


# Funciones de ordenamiento
