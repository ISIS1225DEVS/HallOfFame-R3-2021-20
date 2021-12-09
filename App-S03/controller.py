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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init_catalog():
    return model.init_catalog()

# Funciones para la carga de datos
def load_UFOs(catalog):
    filename = cf.data_dir + 'UFOS-utf8-large.csv'
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for ufo_data in input_file:
        model.add_ufo(catalog, ufo_data)

def create_city_index(catalog):
    model.create_city_index(catalog)
    
def create_duration_index(catalog):
    model.create_duration_index(catalog)

def create_time_index(catalog):
    model.create_time_index(catalog)

def create_date_index(catalog):
    model.create_date_index(catalog)

def create_coord_index(catalog):
    model.create_coord_index(catalog)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def UFOsSize(catalog):
    return model.UFOsSize(catalog)

def indexHeight(catalog,index):
    return model.indexHeight(catalog,index)


def indexSize(catalog,index):
    return model.indexSize(catalog,index)


def minKey(catalog,index):
    return model.minKey(catalog,index)

def maxKey(catalog,index):
    return model.maxKey(catalog,index)


def getSightingsByCity(catalog, city):
    return model.getSightingsByCity(catalog, city)
    
def getSightingsByDuration(catalog,duration_min,duration_max):
    return model.getSightingsByDuration(catalog,duration_min,duration_max)

def getSightingsByTime(catalog, time_min, time_max):
    return model.getSightingsByTime(catalog,time_min,time_max)

def getSightingsByDate(catalog, initial_date, final_date):
    return model.getSightingsByDate(catalog, initial_date,final_date)


def getSightingsByGeography(catalog,longitude_min,longitude_max,latitude_min,latitude_max):
    return model.getSightingsByGeography(catalog,longitude_min,longitude_max,latitude_min,latitude_max)