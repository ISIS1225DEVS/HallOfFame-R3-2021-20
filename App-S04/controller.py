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

def initCatalogo():
    return model.initCatalogo()

# Funciones para la carga de datos

def cargarDatos(catalogo, datos):
    
    datos = cf.data_dir + datos
    archivo_datos = csv.DictReader(open(datos, encoding="utf-8"),
                                delimiter=",")
    
    for dato in archivo_datos:
        model.agregarDato(catalogo, dato)

        
    model.agregarAvistamientos(catalogo)
        

# Funciones de ordenamiento

def llamarInsertion(datos, identificador):
    resultado = model.insertion(datos, identificador)
    return resultado

def llamarShell(datos, identificador):
    resultado = model.shell(datos, identificador)
    return resultado

def llamarMerge(datos, identificador):
    resultado = model.merge(datos, identificador)
    return resultado

def llamarQuicksort(datos, identificador):
    resultado = model.quicksort(datos, identificador)
    return resultado

# Funciones de consulta sobre el catálogo

def alturaArbol(catalogo):
    return model.alturaArbol(catalogo)


def elementosArbol(catalogo):
    return model.elementosArbol(catalogo)


def infoCiudad(catalogo, ciudad):
    return model.infoCiudad(catalogo, ciudad)


def rangoLLaves(catalogo, hora_inicial, hora_final):
    return model.rangoLLaves(catalogo, hora_inicial, hora_final)


def infoMap(catalogo, i):
    return model.infoMap(catalogo, i)


def obtenerMax(catalogo):
    return model.obtenerMax(catalogo)


def infoPrimerElemento(primerElemento):
    return model.infoPrimerElemento(primerElemento)

def llamarDarNumeroDuracionMaxima(catalogo):
    return model.darNumeroDuracionMaxima(catalogo)

def llamarDarNumeroFechaAntigua(catalogo):
    return model.darNumeroFechaAntigua(catalogo)

def llamarDarRangoLatitudes(lista, lat_min, lat_max):
    return model.darRangoLatitudes(lista, lat_min, lat_max)
