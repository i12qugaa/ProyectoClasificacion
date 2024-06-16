#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Antonio Javier Quintero García y Noelia Ruiz Morón

Modulo encargado de definir la base de conocimiento del dominio de los diferentes tipos de alimentos
"""

from bcClasificacion import *


# DEFINICION DE LA BASE DE CONOCIMIENTO
  
## Clase representativa de todo alimento

# Define los atributos que caracteriza todo alimento

class Alimento(Clase):
    '''Describe los atributos por los que se caracterizará a un alimento.'''
    def __init__(self, nombre=None):
        '''
        @param nombre: Nombre del alimento
        '''
        Clase.__init__(self, nombre=nombre)
        
        self.atOrigen = Atributo('Origen', 'multiple', None, ['','Animal', 'Vegetal'])
        self.atCalorias = Atributo('Calorias (por 100g)', 'float', 'kcal')
        self.atTextura = Atributo('Textura', 'multiple', None, ['','Firme', 'Cremoso'])
        self.atProteinas = Atributo('Proteinas (por 100g)', 'float', 'g')
        self.atributos = [self.atOrigen, self.atCalorias, self.atTextura, self.atProteinas]


## Clase representativa de una naranja

# Define las reglas de clasificación de la naranja

class Naranja(Alimento):
    def __init__(self):
        Alimento.__init__(self, nombre='naranja')
            
        r1 = Rverifica(idRegla='r1', tipo='igual', atributo=self.atOrigen, valorEsperado='Vegetal')
        r2 = Rverifica(idRegla='r2', tipo='rango', atributo=self.atCalorias, valorEsperado=[42, 62])  # Calorías por 100g
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atTextura, valorEsperado='Firme')
        r4 = Rverifica(idRegla='r4', tipo='rango', atributo=self.atProteinas, valorEsperado=[0.6, 1.2]) # Proteínas por 100g

        self.reglas = [r1, r2, r3, r4]

## Clase representativa de yogur

# Define las reglas de clasificación de yogur

class Yogur(Alimento):
    def __init__(self):
        Alimento.__init__(self, nombre='yogur')
             
        r1 = Rverifica(idRegla='r1', tipo='igual', atributo=self.atOrigen, valorEsperado='Animal')
        r2 = Rverifica(idRegla='r2', tipo='rango', atributo=self.atCalorias, valorEsperado=[60, 120])  # Calorías por 100g
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atTextura, valorEsperado='Cremoso')
        r4 = Rverifica(idRegla='r4', tipo='rango', atributo=self.atProteinas, valorEsperado=[3, 14])  # Proteínas por 100g

        self.reglas = [r1, r2, r3, r4]
        
## Clase representativa de huevo

# Define las reglas de clasificación de huevo

class Huevo(Alimento):
    def __init__(self):
        Alimento.__init__(self, nombre='huevo')
             
        r1 = Rverifica(idRegla='r1', tipo='igual', atributo=self.atOrigen, valorEsperado='Animal')
        r2 = Rverifica(idRegla='r2', tipo='rango', atributo=self.atCalorias, valorEsperado=[130, 155])  # Calorías por 100g  # Calorías por 100g
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atTextura, valorEsperado='Firme')
        r4 = Rverifica(idRegla='r4', tipo='rango', atributo=self.atProteinas, valorEsperado=[11, 16])  # Proteínas por 100g

        self.reglas = [r1, r2, r3, r4]
        
## Clase representativa de nuez

# Define las reglas de clasificación de nuez

class Nuez(Alimento):
    def __init__(self):
        Alimento.__init__(self, nombre='nuez')
             
        r1 = Rverifica(idRegla='r1', tipo='igual', atributo=self.atOrigen, valorEsperado='Vegetal')
        r2 = Rverifica(idRegla='r2', tipo='igual', atributo=self.atCalorias, valorEsperado='654')
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atTextura, valorEsperado='Firme')
        r4 = Rverifica(idRegla='r4', tipo='igual', atributo=self.atProteinas, valorEsperado='15')

        self.reglas = [r1, r2, r3, r4]
        

## Clase representativa de manzana

# Define las reglas de clasificación de manzana

class Manzana(Alimento):
    def __init__(self):
        Alimento.__init__(self, nombre='manzana')
             
        r1 = Rverifica(idRegla='r1', tipo='igual', atributo=self.atOrigen, valorEsperado='Vegetal')
        r2 = Rverifica(idRegla='r2', tipo='rango', atributo=self.atCalorias, valorEsperado=[50, 54])
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atTextura, valorEsperado='Firme')
        r4 = Rverifica(idRegla='r4', tipo='rango', atributo=self.atProteinas, valorEsperado=[0.2, 0.4])

        self.reglas = [r1, r2, r3, r4]
        

## Clase representativa de salmon

# Define las reglas de clasificación de salmon

class Salmon(Alimento):
    def __init__(self):
        Alimento.__init__(self, nombre='salmon')
             
        r1 = Rverifica(idRegla='r1', tipo='igual', atributo=self.atOrigen, valorEsperado='Animal')
        r2 = Rverifica(idRegla='r2', tipo='rango', atributo=self.atCalorias, valorEsperado=[178, 208])
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atTextura, valorEsperado='Firme')
        r4 = Rverifica(idRegla='r4', tipo='rango', atributo=self.atProteinas, valorEsperado=[20, 25])

        self.reglas = [r1, r2, r3, r4]
        

## Clase representativa de ternera

# Define las reglas de clasificación de ternera

class Ternera(Alimento):
    def __init__(self):
        Alimento.__init__(self, nombre='ternera')
             
        r1 = Rverifica(idRegla='r1', tipo='igual', atributo=self.atOrigen, valorEsperado='Animal')
        r2 = Rverifica(idRegla='r2', tipo='rango', atributo=self.atCalorias, valorEsperado=[170, 174])
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atTextura, valorEsperado='Firme')
        r4 = Rverifica(idRegla='r4', tipo='rango', atributo=self.atProteinas, valorEsperado=[23, 24])

        self.reglas = [r1, r2, r3, r4] 


## Clase representativa de mantequilla

# Define las reglas de clasificación de mantequilla

class Mantequilla(Alimento):
    def __init__(self):
        Alimento.__init__(self, nombre='mantequilla')
             
        r1 = Rverifica(idRegla='r1', tipo='igual', atributo=self.atOrigen, valorEsperado='Animal')
        r2 = Rverifica(idRegla='r2', tipo='igual', atributo=self.atCalorias, valorEsperado='717')
        r3 = Rverifica(idRegla='r3', tipo='igual', atributo=self.atTextura, valorEsperado='Cremoso')
        r4 = Rverifica(idRegla='r4', tipo='igual', atributo=self.atProteinas, valorEsperado='0.9')

        self.reglas = [r1, r2, r3, r4] 

# Funcion para devolver lista de clases candidatas del dominio Alimento
    
def clases():
    '''
    Crea una lista de clases candidatas de la base de conocimiento.
    '''
    return [Naranja(), Yogur(), Huevo(), Nuez(), Manzana(), Salmon(), Ternera(), Mantequilla()]
