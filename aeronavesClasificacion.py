#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Antonio Javier Quintero García y Noelia Ruiz Morón

Módulo encargado de definir la base de conocimiento del dominio de los diferentes tipos de aeronaves
"""

from bcClasificacion import *


# DEFINICIÓN DE LA BASE DE CONOCIMIENTO

## Clase representativa de aeronave

# Define los atributos que caracterizan a una aeronave

class Aeronave(Clase):
    def __init__(self, nombre=None):
        Clase.__init__(self, nombre=nombre)

        self.atNumeroPasajeros = Atributo('Número de Pasajeros', 'int', 'Nº')
        self.atPropulsion = Atributo('Propulsión', 'multiple', None, ['','Motor', 'Sin motor'])
        self.atFlota = Atributo('Flota', 'multiple', None, ['','Si', 'No'])
        self.atAlturaOperativa = Atributo('Altura operativa', 'multiple', None, ['','Baja', 'Media', 'Alta', 'Espacial'])
        self.atDespegueAterrizaje = Atributo('Despegue y aterrizaje', 'multiple', None, ['','Horizontal', 'Vertical'])
        self.atributos = [self.atNumeroPasajeros, self.atPropulsion, self.atFlota, self.atAlturaOperativa, self.atDespegueAterrizaje]


## Clase representativa de avion

# Define las reglas de clasificación de avion

class Avion(Aeronave):
    def __init__(self):
        Aeronave.__init__(self, nombre='avión')  # Se inicia con el nombre avión

        # Reglas que debe verificar el avión
        r1 = Rverifica(idRegla='r1', tipo='rango', atributo=self.atNumeroPasajeros, valorEsperado=[1, 500])
        r2 = Rverifica(idRegla='r2', tipo='igual', atributo=self.atPropulsion, valorEsperado='Motor')
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atFlota, valorEsperado='No')
        r4 = Rverifica(idRegla='r4', tipo='igual', atributo=self.atAlturaOperativa, valorEsperado='Alta')
        r5 = Rverifica(idRegla='r5', tipo='igual', atributo=self.atDespegueAterrizaje, valorEsperado='Horizontal')

        self.reglas = [r1, r2, r3, r4, r5]


## Clase representativa de helicóptero

# Define las reglas de clasificación de helicóptero

class Helicoptero(Aeronave):
    def __init__(self):
        Aeronave.__init__(self, nombre='helicóptero')  # Se inicia con el nombre helicóptero

        # Reglas que debe verificar el helicóptero
        r1 = Rverifica(idRegla='r1', tipo='rango', atributo=self.atNumeroPasajeros, valorEsperado=[1, 20])
        r2 = Rverifica(idRegla='r2', tipo='igual', atributo=self.atPropulsion, valorEsperado='Motor')
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atFlota, valorEsperado='No')
        r4 = Rverifica(idRegla='r4', tipo='igual', atributo=self.atAlturaOperativa, valorEsperado='Media')
        r5 = Rverifica(idRegla='r5', tipo='igual', atributo=self.atDespegueAterrizaje, valorEsperado='Vertical')
        self.reglas = [r1, r2, r3, r4, r5]


## Clase representativa de aerostato

# Define las reglas de clasificación de aerostato

class Aerostato(Aeronave):
    def __init__(self):
        Aeronave.__init__(self, nombre='aerostato')  # Se inicia con el nombre aerostato

        # Reglas que debe verificar el aerostato
        r1 = Rverifica(idRegla='r1', tipo='rango', atributo=self.atNumeroPasajeros, valorEsperado=[1, 12])
        r2 = Rverifica(idRegla='r2', tipo='igual', atributo=self.atPropulsion, valorEsperado='Sin motor')
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atFlota, valorEsperado='Si')
        r4 = Rverifica(idRegla='r4', tipo='igual', atributo=self.atAlturaOperativa, valorEsperado='Media')
        r5 = Rverifica(idRegla='r5', tipo='igual', atributo=self.atDespegueAterrizaje, valorEsperado='Vertical')
        self.reglas = [r1, r2, r3, r4, r5]


## Clase representativa de planeador

# Define las reglas de clasificación de planeador

class Planeador(Aeronave):
    def __init__(self):
        Aeronave.__init__(self, nombre='planeador')  # Se inicia con el nombre planeador

        # Reglas que debe verificar el planeador
        r1 = Rverifica(idRegla='r1', tipo='rango', atributo=self.atNumeroPasajeros, valorEsperado=[1, 2])
        r2 = Rverifica(idRegla='r2', tipo='igual', atributo=self.atPropulsion, valorEsperado='Sin motor')
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atFlota, valorEsperado='No')
        r4 = Rverifica(idRegla='r4', tipo='igual', atributo=self.atAlturaOperativa, valorEsperado='Baja')
        r5 = Rverifica(idRegla='r5', tipo='igual', atributo=self.atDespegueAterrizaje, valorEsperado='Horizontal')
        self.reglas = [r1, r2, r3, r4, r5]


## Clase representativa de cohete

# Define las reglas de clasificación de cohete

class Cohete(Aeronave):
    def __init__(self):
        Aeronave.__init__(self, nombre='cohete')  # Se inicia con el nombre cohete

        # Reglas que debe verificar el cohete
        r1 = Rverifica(idRegla='r1', tipo='rango', atributo=self.atNumeroPasajeros, valorEsperado=[1, 10])
        r2 = Rverifica(idRegla='r2', tipo='igual', atributo=self.atPropulsion, valorEsperado='Motor')
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atFlota, valorEsperado='No')
        r4 = Rverifica(idRegla='r4', tipo='igual', atributo=self.atAlturaOperativa, valorEsperado='Espacial')
        r5 = Rverifica(idRegla='r5', tipo='igual', atributo=self.atDespegueAterrizaje, valorEsperado='Vertical')
        self.reglas = [r1, r2, r3, r4, r5]



# Funcion para devolver lista de clases candidatas del dominio Aeronaves

def clases():
    '''
    Crea una lista de clases candidatas de la base de conocimiento.
    '''
    return [Avion(), Helicoptero(), Aerostato(), Planeador(), Cohete()]