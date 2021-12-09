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

from folium import plugins
import config as cf
import sys
import controller
import math as mt
import folium
from folium.plugins import BeautifyIcon
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
assert cf
from prettytable import PrettyTable

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printSightingsByCity(total, city):
    num_cities,date_index = total
    print('Hay un total de',num_cities,'donde se presentaron avistamientos de OVNIs.')
    print('-'*80,'\n')
    sightings = om.size(date_index)
    print('-'*80)
    print('Para la ciudad de',city,'se han presentado un total de',sightings,'avistamientos.\n')
    print('-'*80)

    if sightings > 6:
        dates = om.keySet(date_index)
        first_dates = lt.subList(dates,1,3)
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','country','duration (seconds)','shape']
        for date in lt.iterator(first_dates):
            ufo_list = om.get(date_index,date)['value']
            for ufo_data in lt.iterator(ufo_list):
                imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['country'],
                                ufo_data['duration (seconds)'],ufo_data['shape']])
        
                
                
        last_dates = lt.subList(dates,lt.size(dates)-2,3)
        for date in lt.iterator(last_dates):
            ufo_list = om.get(date_index,date)['value']
            for ufo_data in lt.iterator(ufo_list):
                imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['country'],
                                ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)
    else:
        dates = om.keySet(date_index)
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','country','duration (seconds)','shape']
        for date in lt.iterator(dates):
            ufo_list = om.get(date_index,date)['value']
            for ufo_data in lt.iterator(ufo_list):
                imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['country'],
                                ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)

def printSightingsByTime(total):
    last_time, last_sightings, sightings = total
    if lt.size(sightings) > 0:
        print('Se encontraron un total de',lt.size(sightings),'avistamientos en el rango de horas dado.\n')
        imprimir= PrettyTable()
        imprimir.field_names=['date', 'count']
        imprimir.add_row([last_time,last_sightings])
        print(imprimir)
    print('-'*80)

    if lt.size(sightings) > 6:
        first_data = lt.subList(sightings,1,3)
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','state','country','duration (seconds)','shape']
        for ufo_data in lt.iterator(first_data):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])
        
                
                
        last_data = lt.subList(sightings,lt.size(sightings)-2,3)
        for ufo_data in lt.iterator(last_data):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)
    elif lt.size(sightings) > 0:
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','state','country','duration (seconds)','shape','latitude','longitude']
        for ufo_data in lt.iterator(sightings):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)
    else:
        print('No hay avistamientos dentro del rango de horas dado.')


def printSightingsByDuration(total):
    last_duration, last_sightings, sightings = total
    if lt.size(sightings) > 0:
        print('Se encontraron un total de',lt.size(sightings),'avistamientos en el rango de duración dado.\n')
        imprimir= PrettyTable()
        imprimir.field_names=['duration (seconds)', 'count']
        imprimir.add_row([last_duration,last_sightings])
        print(imprimir)
    print('-'*80)

    if lt.size(sightings) > 6:
        first_data = lt.subList(sightings,1,3)
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','state','country','duration (seconds)','shape']
        for ufo_data in lt.iterator(first_data):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])        
                
        last_data = lt.subList(sightings,lt.size(sightings)-2,3)
        for ufo_data in lt.iterator(last_data):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)
    elif lt.size(sightings) > 0:
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','state','country','duration (seconds)','shape','latitude','longitude']
        for ufo_data in lt.iterator(sightings):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)
    else:
        print('No hay avistamientos dentro del rango de duración dado.')

def printSightingsByDate(total,initial_date,final_date):
    dates,final_dates = total
    print('Hay',lt.size(final_dates),'avistamiento(s) de OVNI(s) como más antiguo(s).')
    sightings = lt.size(dates)
    if sightings > 0:
        print('Además, se encontraron un total de',sightings,'avistamientos entre', initial_date,'y',final_date + '.\n')
        imprimir= PrettyTable()
        imprimir.field_names=['date', 'count']
        for ufo_data in lt.iterator(final_dates):
            imprimir.add_row([ ufo_data['datetime'][0:11],lt.size(final_dates)])
            break
        print(imprimir)
    print('-'*80)

    if sightings > 6:
        first_dates = lt.subList(dates,1,3)
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','state','country','duration (seconds)','shape']
        for ufo_data in lt.iterator(first_dates):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])
        
                
                
        last_dates = lt.subList(dates,lt.size(dates)-2,3)
        for ufo_data in lt.iterator(last_dates):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)
    elif sightings > 0:
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','state','country','duration (seconds)','shape']
        for ufo_data in lt.iterator(dates):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)
    else:
        print('No hay avistamientos dentro del rango de fechas dado.')


def printSightingsByGeography(total):
    sightings = lt.size(total)
    if sightings > 0:
        print('Se encontraron un total de',sightings,'avistamientos en la zona geográfica.\n')
    print('-'*80)

    if sightings > 10:
        first_data = lt.subList(total,1,5)
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','state','country','duration (seconds)','shape','latitude','longitude']
        for ufo_data in lt.iterator(first_data):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape'],str(round(float(ufo_data['latitude']),2)),str(round(float(ufo_data['longitude']),2))])
        
                
                
        last_data = lt.subList(total,lt.size(total)-4,5)
        for ufo_data in lt.iterator(last_data):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape'],str(round(float(ufo_data['latitude']),2)),str(round(float(ufo_data['longitude']),2))])
        print(imprimir)
    elif sightings > 0:
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','state','country','duration (seconds)','shape','latitude','longitude']
        for ufo_data in lt.iterator(total):
            imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['state'],ufo_data['country'],
                            ufo_data['duration (seconds)'],ufo_data['shape'],str(round(float(ufo_data['latitude']),2)),str(round(float(ufo_data['longitude']),2))])
        print(imprimir)
    else:
        print('No hay avistamientos dentro de la zona geográfica.')

def createSightingsMap(data,total):
    longitude_min,longitude_max,latitude_min,latitude_max=data
    longitude = (mt.floor(float(longitude_min)) + mt.ceil(float(longitude_max)))/2
    latitude= (mt.floor(float(latitude_min)) + mt.ceil(float(latitude_max)))/2
    
    m = folium.Map(location=[latitude,longitude], zoom_start=5)
    folium.Rectangle([(float(latitude_max),float(longitude_max)),(float(latitude_min),float(longitude_min))],color="#3186cc",fill=True,fill_color="#3186cc").add_to(m)
    tooltip = 'More Info'
    for sighting in lt.iterator(total):
        iframe = folium.IFrame('Date: ' + sighting['datetime'] + '<br>' + 'City: ' + sighting['city'] + '<br>' + 'Country: ' + sighting['country'] + '<br>' + 'Duration (seconds): ' + sighting['duration (seconds)'] + '<br>' + 'Shape: ' + sighting['shape'])
        popup = folium.Popup(iframe, min_width=200, max_width=300)
        folium.Marker([sighting['latitude'], sighting['longitude']], popup=popup, tooltip=tooltip).add_to(m)
    m.save('index.html')


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- Contar los avistamientos en una ciudad")
    print("4- Contar los avistamientos en un rango de duración")
    print("5- Contar los avistamientos por Hora/Minuto del día")
    print("6- Contar los avistamientos en un rango de fechas")
    print("7- Contar los avistamientos en una zona geográficas")
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.init_catalog()
    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos de ovnis ....")
        controller.load_UFOs(cont)
        print('Avistamientos de ovnis cargados: ' + str(controller.UFOsSize(cont)))
        input('Presione "Enter" para continuar.')
    elif int(inputs[0]) == 3:
        print("\nBuscando y listando cronológicamente los avistamientos en una ciudad")
        city = input("Nombre de la ciudad a consultar: ")
        controller.create_city_index(cont)
        total = controller.getSightingsByCity(cont, city)
        index = 'city_index'
        print('-'*80)
        print('Altura del arbol: ' + str(controller.indexHeight(cont,index)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont,index)))
        print('Menor Llave: ' + str(controller.minKey(cont,index)))
        print('Mayor Llave: ' + str(controller.maxKey(cont,index)))
        print('-'*80,'\n')
        print('-'*80)
        printSightingsByCity(total, city)
        input('Presione "Enter" para continuar.')
    elif int(inputs[0]) == 4:
        print("\nBuscando y listando los avistamientos por rango de duración.")
        duration_min = round(float(input("Duración inicial del rango: ")),1)
        duration_max= round(float(input("Duración final del rango: ")),1)
        controller.create_duration_index(cont)
        total = controller.getSightingsByDuration(cont,duration_min,duration_max)
        index = 'duration_index'
        print('-'*80)
        print('Altura del arbol: ' + str(controller.indexHeight(cont,index)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont,index)))
        print('Menor Llave: ' + str(controller.minKey(cont,index)))
        print('Mayor Llave: ' + str(controller.maxKey(cont,index)))
        print('-'*80,'\n')
        print('-'*80)
        printSightingsByDuration(total)
        input('Presione "Enter" para continuar.')
    elif int(inputs[0]) == 5:
        print("\nBuscando y listando los avistamientos por Hora/Minutos del día.")
        time_min = input("Tiempo inicial del rango (HH:MM): ")+":00"
        time_max= input("Tiempo final del rango (HH:MM): ")+":00"
        controller.create_time_index(cont)
        total = controller.getSightingsByTime(cont,time_min,time_max)
        index = 'time_index'
        print('-'*80)
        print('Altura del arbol: ' + str(controller.indexHeight(cont,index)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont,index)))
        print('Menor Llave: ' + str(controller.minKey(cont,index)))
        print('Mayor Llave: ' + str(controller.maxKey(cont,index)))
        print('-'*80,'\n')
        print('-'*80)
        printSightingsByTime(total)
        input('Presione "Enter" para continuar.')
    elif int(inputs[0]) == 6:
        print("\nBuscando y listando cronológicamente los avistamientos en un rango de fechas.")
        initial_date = input("Fecha inicial del rango: ")
        final_date = input("Fecha final del rango: ")
        controller.create_date_index(cont)
        total = controller.getSightingsByDate(cont, initial_date, final_date)
        index = 'date_index'
        print('-'*80)
        print('Altura del arbol: ' + str(controller.indexHeight(cont,index)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont,index)))
        print('Menor Llave: ' + str(controller.minKey(cont,index)))
        print('Mayor Llave: ' + str(controller.maxKey(cont,index)))
        print('-'*80,'\n')
        print('-'*80)
        printSightingsByDate(total, initial_date, final_date)
        input('Presione "Enter" para continuar.')
    elif int(inputs[0]) == 7:
        print("\nBuscando y listando los avistamientos para una zona geográfica.")
        longitude_min = input("Longitud inicial de la zona geográfica: ")
        longitude_max= input("Longitud final de la zona geográfica: ")
        latitude_min = input("Latitud inicial de la zona geográfica: ")
        latitude_max = input("Latitud final de la zona geográfica: ")
        data = [longitude_min,longitude_max,latitude_min,latitude_max]
        controller.create_coord_index(cont)
        total = controller.getSightingsByGeography(cont,longitude_min,longitude_max,latitude_min,latitude_max)
        index = 'coord_index'
        print('-'*80)
        print('Altura del arbol: ' + str(controller.indexHeight(cont,index)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont,index)))
        print('Menor Llave: ' + str(controller.minKey(cont,index)))
        print('Mayor Llave: ' + str(controller.maxKey(cont,index)))
        print('-'*80,'\n')
        print('-'*80)
        printSightingsByGeography(total)
        input('Presione "Enter" para continuar.')
        createSightingsMap(data,total)
        input('Presione "Enter" para continuar.')

    else:
        sys.exit(0)
sys.exit(0)
