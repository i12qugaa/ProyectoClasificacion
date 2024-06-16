#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Antonio Javier Quintero García y Noelia Ruiz Morón

Modulo encargado de definir las clases fundamentales para la base de conocimiento de un sistema de clasificacion
"""

import types
from PyQt5.QtWidgets import QWidget

# CLASE GENERICA PARA REPRESENTACION DE ENTIDADES
class Clase:
    '''Clase en la jerarquia mas alta.'''
    def __init__(self, nombre):
        '''
        @param: Nombre de la clase.
        '''
        self.nombre = nombre  # La clase tiene un nombre
        self.reglas = []  # Lista de reglas que caracteriza a la clase
        
    def descripcion(self):
        '''Devuelve el texto de la descripcion de una clase.'''
        descripcion = self.nombre + '\n'
        for r in self.reglas:
            descripcion += f"{r.idRegla} {r.tipo} None {r.atributo.nombre} "
            if isinstance(r.valorEsperado, str):
                descripcion += f" {r.valorEsperado}\n"
            elif isinstance(r.valorEsperado, (int, float)):
                descripcion += f" {r.valorEsperado}\n"
            elif isinstance(r.valorEsperado, list):
                descripcion += ' '.join(str(i) for i in r.valorEsperado) + '\n'
        return descripcion

# CLASE GENERICA PARA REPRESENTACION DE REGLAS Y DEFINICION DE TIPOS DE REGLAS
class Regla:
    '''Describe aspectos generales de una regla.'''
    def __init__(self, idRegla, tipo):
        self.idRegla = idRegla
        self.tipo = tipo

class Rverifica(Regla):
    '''Esta regla verifica si los valores de un atributo satisfacen las restricciones de la regla de la clase.'''
    def __init__(self, idRegla, tipo, atributo, valorEsperado):
        super().__init__(idRegla, tipo)
        self.atributo = atributo
        self.valorEsperado = valorEsperado

    def execute(self, at):
        '''Verifica que un atributo-valor satisface la regla de una clase.'''
        if self.atributo.nombre == at.atributo.nombre:
            if self.tipo == 'igual':
                return self.valorEsperado == at.valor
            if self.tipo == 'rango':
                return self.valorEsperado[1] >= at.valor >= self.valorEsperado[0]
        return None
            
    def descripcion(self):
        descripcion = ''
        descripcion += f"idRegla: {self.idRegla}\n"
        descripcion += f"Tipo: {self.tipo}\n"
        descripcion += f"Atributo: {self.atributo.nombre}\n"
        if isinstance(self.valorEsperado, str):
            descripcion += f"Valor esperado: {self.valorEsperado}\n"
        elif isinstance(self.valorEsperado, (int, float)):
            descripcion += f"Valor esperado: {self.valorEsperado}\n"
        elif isinstance(self.valorEsperado, list):
            descripcion += ' '.join(f"Valor esperado: {ve}" for ve in self.valorEsperado)
        return descripcion

# CLASE GENERICA PARA REPRESENTACION DE ATRIBUTOS
class Atributo:
    '''Clase Atributo. Permite especificar las propiedades de los atributos que van a usarse en la base de conocimiento para describir un objeto.'''
    def __init__(self, nombre, tipo, unidad, posiblesValores=None):
        self.nombre = nombre
        self.tipo = tipo
        self.unidad = unidad

        # Obtenemos los posibles valores del atributo en caso de que sea de tipo multiple
        if tipo == 'multiple' and posiblesValores is not None and isinstance(posiblesValores, list):
            self.posiblesValores = posiblesValores 
            

# CLASE GENERICA PARA REPRESENTACION DE CARACTERISTICAS
class Caracteristica:
    '''Par atributo-valor de un objeto concreto'''
    def __init__(self, atributo, valor):
        self.atributo = atributo
        self.valor = valor

# CLASE GENERICA PARA REPRESENTACION DE OBJETOS
class Objeto:
    '''Aquello que se desconoce y se quiere clasificar'''
    def __init__(self, identificador, caracteristicas):
        '''Se inicia la clase especificando el nombre y los atributos del objeto.'''
        self.identificador = identificador
        self.caracteristicas = caracteristicas
        self.clase = None

    def describeObjeto(self):
        print(f'Identificador: {self.identificador}')
        for ct in self.caracteristicas:
            print(f'{ct.atributo.nombre} {ct.atributo.tipo} {ct.valor} {ct.atributo.unidad}')
