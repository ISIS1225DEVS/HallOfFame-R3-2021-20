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
#======================================
# Inicialización del Catálogo de libros
#======================================
def init():
    analyzer = model.newAnalyzer()
    
    return analyzer

#=================================
# Funciones para la carga de datos
#=================================
def loadData(analyzer, ufosfile):
    ufosfile = cf.data_dir + ufosfile
    input_file = csv.DictReader(open(ufosfile, encoding="utf-8"),
                                delimiter=",")
    for ufo in input_file:
        model.addUfo(analyzer, ufo)
    
    return analyzer

#===================================
#Funciones para la creación de datos
#===================================
def getUfosByCity(mapa, ciudad):

    return model.getUfosByCity(mapa, ciudad)

def getUfosByDuration(mapa, limit_inf, limit_sup):

    return model.getUfosByDuration(mapa, limit_inf, limit_sup)

def getUfosByTime(mapa, limit_inf, limit_sup):

    return model.getUfosByTime(mapa, limit_inf, limit_sup)

def getUfosByDatetime(mapa, limit_inf, limit_sup):

    return model.getUfosByDatetime(mapa, limit_inf, limit_sup)

def getUfosByLonLat(mapa, lon_inf, lon_sup, lat_inf, lat_sup):

    return model.getUfosByLonLat(mapa, lon_inf, lon_sup, lat_inf, lat_sup)

#==========================
# Funciones de ordenamiento
#==========================

#========================================
# Funciones de consulta sobre el catálogo
#========================================
def requerimiento1(mapa, ufo):

    return model.requerimiento1(mapa, ufo)

def requerimiento2(mapa, ufo):

    return model.requerimiento2(mapa, ufo)

def requerimiento3(mapa, ufo):

    return model.requerimiento3(mapa, ufo)

def requerimiento4(mapa, ufo):

    return model.requerimiento4(mapa, ufo)

def requerimiento5(mapa, ufo):

    return model.requerimiento5(mapa, ufo)
    
def requerimiento6(latitud, longitud, ufos):
    
    return model.requerimiento6(latitud, longitud, ufos)

def ufosSize(analyzer):
    
    return model.ufosSize(analyzer)
    