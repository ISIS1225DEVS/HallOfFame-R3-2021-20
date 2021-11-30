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
 """

import config as cf
import model
import time
import csv


###############################################################################################################
# Inicialización del Catálogo de Avistamiento
###############################################################################################################

def initialization():
    return model.initialization()

###############################################################################################################
# Funciones para la carga de datos
###############################################################################################################

def loadData(catalog, sample_size):
    sightings_data = cf.data_dir + 'UFOS/UFOS-utf8-large.csv'
    input_file = csv.DictReader(open(sightings_data, encoding="utf-8"), delimiter=",")
    reduced_list = list(input_file)[:sample_size]

    for event in reduced_list:
        model.addCity(catalog, event)
        model.addDuration(catalog, event)
        model.addTime(catalog, event)
        model.addDate(catalog, event)
        model.addCoordinate(catalog, event)

    return catalog

###############################################################################################################
# Funciones de consulta sobre el catálogo
###############################################################################################################

def Requirement1(catalog, city):
    start_time = time.process_time()

    information = model.Requirement1(catalog, city)

    first_events_list = information[0]
    last_events_list = information[1]
    num_cities = information[2]
    most_events_city = information[3]
    num_events_city = information[4]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 

    return elapsed_time, first_events_list, last_events_list, num_cities, most_events_city, num_events_city

###############################################################################################################

def Requirement2(catalog, initial_duration, end_duration):
    start_time = time.process_time()

    information = model.Requirement2(catalog, initial_duration, end_duration)

    first_events_list = information[0]
    last_events_list = information[1]
    num_durations = information[2]
    longest_duration = information[3]
    num_events_longest_duration = information[4]
    num_events_duration_interval = information[5]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 

    return elapsed_time, first_events_list, last_events_list, num_durations, longest_duration, num_events_longest_duration, num_events_duration_interval

###############################################################################################################

def Requirement3(catalog, initial_time, end_time):
    start_time = time.process_time()

    information = model.Requirement3(catalog, initial_time, end_time)

    first_events_list = information[0]
    last_events_list = information[1]
    num_times = information[2]
    latest_time = information[3]
    num_events_latest_time = information[4]
    num_events_time_interval = information[5]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 

    return elapsed_time, first_events_list, last_events_list, num_times, latest_time, num_events_latest_time, num_events_time_interval

###############################################################################################################

def Requirement4(catalog, initial_date, end_date):
    start_time = time.process_time()

    information = model.Requirement4(catalog, initial_date, end_date)

    first_events_list = information[0]
    last_events_list = information[1]
    num_dates = information[2]
    oldest_date = information[3]
    num_events_oldest_date = information[4]
    num_events_date_interval = information[5]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 

    return elapsed_time, first_events_list, last_events_list, num_dates, oldest_date, num_events_oldest_date, num_events_date_interval

###############################################################################################################

def Requirement5(catalog, initial_longitude, end_longitude, initial_latitude, end_latitude):
    start_time = time.process_time()

    information = model.Requirement5(catalog, initial_longitude, end_longitude, initial_latitude, end_latitude)

    first_events_list = information[0]
    last_events_list = information[1]
    num_events_area = information[2]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 

    return elapsed_time, first_events_list, last_events_list, num_events_area

###############################################################################################################

def Requirement6(catalog, initial_longitude, end_longitude, initial_latitude, end_latitude):
    start_time = time.process_time()

    area_events_list = model.Requirement6(catalog, initial_longitude, end_longitude, initial_latitude, end_latitude)

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 

    return elapsed_time, area_events_list