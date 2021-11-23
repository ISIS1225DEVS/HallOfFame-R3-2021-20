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
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo
def initCatalog():
    return model.newCatalog()

# Funciones para la carga de datos
def loadData(catalog, file):
    file = cf.data_dir + file
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for avist in input_file:
        model.addAvist(catalog, avist)
    return catalog

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def countSightingsCity(catalog, city):
    return model.countSightingsCity(catalog, city) 

def countSightingsDuration(catalog ,lower, upper):
    return model.countSightingsDuration(catalog,lower, upper)

def sightingsByHour(catalog, ihour, fhour):
    return model.sightingsByHour(catalog, ihour, fhour)

def countSightingsDateRange(catalog, lowDate, upDate):
    return model.countSightingsDateRange(catalog, lowDate, upDate)

def countSightingsZone(catalog, latmin, latmax, longmin, longmax):
    return model.countSightingsZone(catalog, latmin, latmax, longmin, longmax)

def createMapReq5(catalog, latmin, latmax, longmin, longmax):
    return model.createMapReq5(catalog, latmin, latmax, longmin, longmax)