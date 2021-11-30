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
 
from DISClib.DataStructures import mapentry as me
import DISClib.Algorithms.Trees.traversal as trv
from DISClib.DataStructures import bst as bst
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from datetime import datetime
import config as cf
assert cf

###############################################################################################################
# Construccion de modelos
###############################################################################################################

def initialization():
    catalog = { 'cities_list': None,
                'cities_map': None,
                'durations_map': None,
                'durations_BST': None,
                'times_map': None,
                'times_BST': None,
                'dates_map': None,
                'dates_BST': None,
                'latitudes_map': None,
                'latitudes_BST': None}
    catalog['cities_map'] = mp.newMap(19900, maptype='PROBING', loadfactor=0.5)
    catalog['cities_list'] = lt.newList('ARRAY_LIST')
    catalog['durations_map'] = mp.newMap(533, maptype='PROBING', loadfactor=0.5)
    catalog['durations_BST'] = bst.newMap(cmpFunction1)
    catalog['times_map'] = mp.newMap(1390, maptype='PROBING', loadfactor=0.5)
    catalog['times_BST'] = bst.newMap(cmpFunction1)
    catalog['dates_map'] = mp.newMap(10525, maptype='PROBING', loadfactor=0.5)
    catalog['dates_BST'] = bst.newMap(cmpFunction1)
    catalog['latitudes_map'] = mp.newMap(3842, maptype='PROBING', loadfactor=0.5)
    catalog['latitudes_BST'] = bst.newMap(cmpFunction1)

    return catalog

###############################################################################################################
# Funciones para agregar informacion al catalogo
###############################################################################################################

def addCity(catalog, event):
    city = event['city']
    cities_map = catalog['cities_map']
    cities_list = catalog['cities_list']
    event_date = datetime.strptime(event['datetime'], "%Y-%m-%d %H:%M:%S")

    if mp.contains(cities_map, city):
        city_events_BST = me.getValue(mp.get(cities_map, city))
        bst.put(city_events_BST, event_date, event)

    else:
        city_events_BST = bst.newMap(cmpFunction2)
        bst.put(city_events_BST, event_date, event)
        mp.put(cities_map, city, city_events_BST)
        lt.addLast(cities_list, city)

###############################################################################################################

def addDuration(catalog, event):
    city = event['city']
    country = event['country']
    country_city = city + country
    duration = event['duration (seconds)']
    durations_map = catalog['durations_map']
    durations_BST = catalog['durations_BST']

    if mp.contains(durations_map, duration):
        duration_events_BST = me.getValue(mp.get(durations_map, duration))
        bst.put(duration_events_BST, country_city, event)
    else:
        duration_events_BST = bst.newMap(cmpFunction2)
        bst.put(duration_events_BST, country_city, event)
        mp.put(durations_map, duration, duration_events_BST)
        bst.put(durations_BST, float(duration), float(duration))

###############################################################################################################

def addTime(catalog, event):
    times_map = catalog['times_map']
    times_BST = catalog['times_BST']
    event_date_info = event['datetime']
    event_date = datetime.strptime(event_date_info[:10], "%Y-%m-%d")
    event_time = datetime.strptime(event_date_info[11:], "%H:%M:%S")

    if mp.contains(times_map, str(event_time)):
        time_events_BST = me.getValue(mp.get(times_map, str(event_time)))
        bst.put(time_events_BST, event_date, event)
    else:
        time_events_BST = bst.newMap(cmpFunction2)
        bst.put(time_events_BST, event_date, event)
        mp.put(times_map, str(event_time), time_events_BST)
        bst.put(times_BST, event_time, event_time)

###############################################################################################################

def addDate(catalog, event):
    dates_map = catalog['dates_map']
    dates_BST = catalog['dates_BST']
    event_date_info = event['datetime']
    event_date = datetime.strptime(event_date_info[:10], "%Y-%m-%d")
    event_time = datetime.strptime(event_date_info[11:], "%H:%M:%S")

    if mp.contains(dates_map, str(event_date)):
        date_events_BST = me.getValue(mp.get(dates_map, str(event_date)))
        bst.put(date_events_BST, event_time, event)
    else:
        date_events_BST = bst.newMap(cmpFunction2)
        bst.put(date_events_BST, event_time, event)
        mp.put(dates_map, str(event_date), date_events_BST)
        bst.put(dates_BST, event_date, event_date)

###############################################################################################################

def addCoordinate(catalog, event):
    latitudes_map = catalog['latitudes_map']
    latitudes_BST = catalog['latitudes_BST']
    event_longitude = round(float(event['longitude']), 2)
    event_latitude = round(float(event['latitude']), 2)

    if mp.contains(latitudes_map, str(event_latitude)):
        latitude_events_BST = me.getValue(mp.get(latitudes_map, str(event_latitude)))
        bst.put(latitude_events_BST, event_longitude, (event_longitude, event))
    else:
        latitude_events_BST = bst.newMap(cmpFunction2)
        bst.put(latitude_events_BST, event_longitude, (event_longitude, event))
        mp.put(latitudes_map, str(event_latitude), latitude_events_BST)
        bst.put(latitudes_BST, event_latitude, event_latitude)

###############################################################################################################
# Funciones para creacion de datos
###############################################################################################################

def getFirstandLastElements(lst, num_positions, comparition):
    num_elements_list = lt.size(lst)

    if num_elements_list > num_positions*2:
        if comparition == '>':
            first_events_list = lt.iterator(lt.subList(lst, 1, num_positions))
            last_events_list = lt.iterator(lt.subList(lst, num_elements_list - (num_positions - 1), num_positions))
        else:
            last_events_list = lt.iterator(lt.subList(lst, 1, num_positions))
            first_events_list = lt.iterator(lt.subList(lst, num_elements_list - (num_positions - 1), num_positions))
    else:
        first_events_list = lt.iterator(lst)
        last_events_list = lt.iterator(lt.newList())

    return first_events_list, last_events_list, num_elements_list

###############################################################################################################

def getElementsIntervalValues(elements_map, values_list, previous_value, num_values, initial_value, end_value):
    if initial_value > end_value:
        temporal_end_value = end_value
        end_value = initial_value
        initial_value = temporal_end_value

    index = 1
    interval_values_elements_list = lt.newList('ARRAY_LIST')
    while index <= num_values and previous_value < end_value:
        value = lt.getElement(values_list, index)

        if initial_value <= value and value <= end_value:
            value_elements_list = trv.inorder(me.getValue(mp.get(elements_map, str(value))))
            for elements in lt.iterator(value_elements_list):
                lt.addLast(interval_values_elements_list, elements)
        index += 1
        previous_value == value

    return interval_values_elements_list

###############################################################################################################

def getMostElement(lst, map_list, comparition):
    num_elements_list = lt.size(lst)

    if comparition == '>':
        most_element = lt.getElement(lst, num_elements_list)
    else:
        most_element = lt.getElement(lst, 1)

    size_most_element_value = bst.size(me.getValue(mp.get(map_list, str(most_element))))

    return most_element, size_most_element_value, num_elements_list

###############################################################################################################

def getElementsDoubleIntervalValues(elements_map, values_list, previous_value_1, previous_value_2, num_values,
                                                    initial_value_1, end_value_1, initial_value_2, end_value_2):
    if initial_value_1 > end_value_1:
        temporal_end_value_1 = end_value_1
        end_value_1 = initial_value_1
        initial_value_1 = temporal_end_value_1
    if initial_value_2 > end_value_2:
        temporal_end_value_2 = end_value_2
        end_value_2 = initial_value_2
        initial_value_2 = temporal_end_value_2

    index_1 = 1
    interval_values_elements_list = lt.newList('ARRAY_LIST')
    while index_1 <= num_values and previous_value_1 < end_value_1:
        value_1 = lt.getElement(values_list, index_1)

        if initial_value_1 <= value_1 and value_1 <= end_value_1:
            values_list_2 = trv.inorder(me.getValue(mp.get(elements_map, str(value_1))))
            num_longitudes = lt.size(values_list_2)
            index_2 = 1
            while index_2 <= num_longitudes and previous_value_2 < end_value_2:
                element_info = lt.getElement(values_list_2, index_2)
                value_2 = element_info[0]
    
                if initial_value_2 <= value_2 and value_2 <= end_value_2:
                    element = element_info[1]
                    lt.addLast(interval_values_elements_list, element)

                index_2 += 1
                previous_value_2 == value_2
        index_1 += 1
        previous_value_1 == value_1

    return interval_values_elements_list

###############################################################################################################
# Funciones utilizadas para comparar elementos dentro de una lista
###############################################################################################################

def cmpFunction1(key_node_1, key_node_2):
    if key_node_1 > key_node_2:
        return 1
    elif key_node_1 < key_node_2:
        return -1
    else:
        return 0

###############################################################################################################

def cmpFunction2(key_node_1, key_node_2):
    if key_node_1 > key_node_2:
        return 1
    elif key_node_1 < key_node_2:
        return -1
    else:
        return 1

###############################################################################################################
# Funciones de consulta
###############################################################################################################

def Requirement1(catalog, city):
    cities_map = catalog['cities_map']
    cities_list = catalog['cities_list']
    num_cities = lt.size(cities_list)

    if mp.contains(cities_map, city):
        city_events_list = trv.inorder(me.getValue(mp.get(cities_map, city)))
        city_events_info = getFirstandLastElements(city_events_list, 3, '>')
        first_events_list = city_events_info[0]
        last_events_list = city_events_info[1]
        num_events_city = city_events_info[2]

        num_events_most_city = -1
        for city in lt.iterator(cities_list):
            num_events_particular_city = bst.size(me.getValue(mp.get(cities_map, city)))
            if num_events_particular_city > num_events_most_city:
                num_events_most_city = num_events_particular_city
                most_events_city = city
    else:
        first_events_list = lt.iterator(lt.newList())
        last_events_list = first_events_list
        most_events_city = 'None'
        num_events_city = 0

    return first_events_list, last_events_list, num_cities, most_events_city, num_events_city

###############################################################################################################

def Requirement2(catalog, initial_duration, end_duration):
    durations_map = catalog['durations_map']
    durations_BST = catalog['durations_BST']
    durations_list = trv.inorder(durations_BST)

    longest_duration_info = getMostElement(durations_list, durations_map, '>')
    longest_duration = longest_duration_info[0]
    num_events_longest_duration = longest_duration_info[1]
    num_durations = longest_duration_info[2]

    previous_duration = -1
    duration_interval_events_list = getElementsIntervalValues(durations_map, durations_list, 
                                            previous_duration, num_durations, initial_duration, end_duration)
            
    duration_interval_events_info = getFirstandLastElements(duration_interval_events_list, 3, '>')
    first_events_list = duration_interval_events_info[0]
    last_events_list = duration_interval_events_info[1]
    num_events_duration_interval = duration_interval_events_info[2]

    return first_events_list, last_events_list, num_durations, longest_duration, num_events_longest_duration, num_events_duration_interval

###############################################################################################################

def Requirement3(catalog, initial_time, end_time):
    times_map = catalog['times_map']
    times_BST = catalog['times_BST']
    times_list = trv.inorder(times_BST)
    initial_time = datetime.strptime(initial_time, "%H:%M:%S")
    end_time = datetime.strptime(end_time, "%H:%M:%S")

    latest_time_info = getMostElement(times_list, times_map, '>')
    latest_time = latest_time_info[0]
    num_events_latest_time = latest_time_info[1]
    num_times = latest_time_info[2]

    previous_time = datetime.strptime('00:00:00', "%H:%M:%S")
    time_interval_events_list = getElementsIntervalValues(times_map, times_list, previous_time, num_times,
                                                                                        initial_time, end_time)
            
    time_interval_events_info = getFirstandLastElements(time_interval_events_list, 3, '>')
    first_events_list = time_interval_events_info[0]
    last_events_list = time_interval_events_info[1]
    num_events_time_interval = time_interval_events_info[2]

    return first_events_list, last_events_list, num_times, latest_time, num_events_latest_time, num_events_time_interval

###############################################################################################################

def Requirement4(catalog, initial_date, end_date):
    dates_map = catalog['dates_map']
    dates_BST = catalog['dates_BST']
    dates_list = trv.inorder(dates_BST)
    initial_date = datetime.strptime(initial_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    oldest_date_info = getMostElement(dates_list, dates_map, '<')
    oldest_date = oldest_date_info[0]
    num_events_oldest_date = oldest_date_info[1]
    num_dates = oldest_date_info[2]

    previous_date = datetime.strptime('00:00:00', "%H:%M:%S")
    date_interval_events_list = getElementsIntervalValues(dates_map, dates_list, previous_date, num_dates,
                                                                                        initial_date, end_date)

    date_interval_events_info = getFirstandLastElements(date_interval_events_list, 3, '>')
    first_events_list = date_interval_events_info[0]
    last_events_list = date_interval_events_info[1]
    num_events_date_interval = date_interval_events_info[2]

    return first_events_list, last_events_list, num_dates, oldest_date, num_events_oldest_date, num_events_date_interval

###############################################################################################################

def Requirement5(catalog, initial_longitude, end_longitude, initial_latitude, end_latitude):
    latitudes_map = catalog['latitudes_map']
    latitudes_BST = catalog['latitudes_BST']
    latitudes_list = trv.inorder(latitudes_BST)
    num_latitudes = bst.size(latitudes_BST)

    previous_value_latitude = -181
    previous_value_longitude = -181

    area_events_list = getElementsDoubleIntervalValues(latitudes_map, latitudes_list, 
            previous_value_latitude, previous_value_longitude, num_latitudes, initial_latitude, end_latitude,
            initial_longitude, end_longitude)

    area_interval_events_info = getFirstandLastElements(area_events_list, 5, '>')
    first_events_list = area_interval_events_info[0]
    last_events_list = area_interval_events_info[1]
    num_events_area = area_interval_events_info[2]

    return first_events_list, last_events_list, num_events_area

###############################################################################################################

def Requirement6(catalog, initial_longitude, end_longitude, initial_latitude, end_latitude):
    latitudes_map = catalog['latitudes_map']
    latitudes_BST = catalog['latitudes_BST']
    latitudes_list = trv.inorder(latitudes_BST)
    num_latitudes = bst.size(latitudes_BST)

    previous_value_latitude = -181
    previous_value_longitude = -181

    area_events_list = lt.iterator(getElementsDoubleIntervalValues(latitudes_map, latitudes_list, 
            previous_value_latitude, previous_value_longitude, num_latitudes, initial_latitude, end_latitude,
            initial_longitude, end_longitude))

    return area_events_list