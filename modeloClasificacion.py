#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Antonio Javier Quintero García y Noelia Ruiz Morón

Módulo encargado de definir el modelo de aplicación del sistema de clasificación.
"""

from bcClasificacion import *
import aeronavesClasificacion as bc_aeronaves
import alimentosClasificacion as bc_alimentos


class MetodoPoda:
    def __init__(self, objeto, dominio):
        self.objeto = objeto
        self.dominio = dominio
        self.clases_candidatas = []
        self.lista_atributos_usados = []
        self.conjunto_nuevos_valores = []
        self.explicacion = ''

    def execute(self):
        # Generar las posibles clases candidatas
        generar = Generar(self.dominio)
        self.clases_candidatas = generar.execute()
        self.explicacion += 'Se generaron las clases candidatas que son:\n'
        for clase_candidata in self.clases_candidatas:
            self.explicacion += f'{clase_candidata.nombre}\n'
        self.explicacion += '\n'

        nueva_solucion = True
        # La condición self.clases_candidatas dentro del while indica que la longitud de las clases candidatas debe ser mayor a 0
        while nueva_solucion and self.clases_candidatas:
            especificar = Especificar(self.clases_candidatas, self.lista_atributos_usados)
            nuevo_atributo, lista_actualizada = especificar.execute()

            if nuevo_atributo:
                self.lista_atributos_usados = lista_actualizada
                self.explicacion += f'Seleccionamos el atributo {nuevo_atributo.nombre}\n'

                # Obtenemos el valor del atributo en el objeto
                obtener = Obtener(self.objeto, nuevo_atributo)
                caracteristica = obtener.execute()
                self.explicacion += f'{caracteristica.valor}\n'
                self.conjunto_nuevos_valores.append(caracteristica)

                nuevas_clases_candidatas = []
                for clase_candidata in self.clases_candidatas:
                    self.explicacion += f'\tProbamos la clase candidata {clase_candidata.nombre}\n'
                    equiparar = Equiparar(clase_candidata, self.conjunto_nuevos_valores)
                    resultado, explicacion = equiparar.execute()
                    self.explicacion += explicacion
                    self.explicacion += f'\tResultado de equiparar clase candidata {clase_candidata.nombre}: {resultado}\n'

                    if resultado:
                        nuevas_clases_candidatas.append(clase_candidata)
            else:
                nueva_solucion = False

            self.clases_candidatas = nuevas_clases_candidatas
            self.explicacion += 'Clases candidatas tras la equiparación: '
            for clase_candidata in self.clases_candidatas:
                self.explicacion += f' {clase_candidata.nombre} '
                self.explicacion += f'\n{clase_candidata.descripcion()}\n'
            self.explicacion += '\n'

        return self.clases_candidatas, self.explicacion
    

class Inferencia:
    def __init__(self):
        pass

    def execute(self):
        pass

class Generar(Inferencia):
    def __init__(self, dominio):
        super().__init__()
        self.dominio = dominio

    def execute(self):
        if self.dominio == 'Aeronaves':
            return bc_aeronaves.clases()
        elif self.dominio == 'Alimentos':
            return bc_alimentos.clases()
        else:
            return None

    
class Especificar(Inferencia):
    def __init__(self, clases_candidatas, lista_atributos_usados):
        super().__init__()
        self.clases_candidatas = clases_candidatas
        self.lista_atributos_usados = lista_atributos_usados

    def execute(self):
        if self.clases_candidatas:
            clase = self.clases_candidatas[0]
            for atributo in clase.atributos:
                if atributo.nombre not in (atu.nombre for atu in self.lista_atributos_usados):
                    self.lista_atributos_usados.append(atributo)
                    return atributo, self.lista_atributos_usados
        return None, None

    
class Obtener(Inferencia):
    def __init__(self, objeto, atributo):
        super().__init__()
        self.objeto = objeto
        self.atributo = atributo

    def execute(self):
        for caracteristica in self.objeto.caracteristicas:
            if self.atributo.nombre == caracteristica.atributo.nombre:
                return caracteristica
        return None
   

class Equiparar(Inferencia):
    def __init__(self, candidata, nuevos_valores):
        super().__init__()
        self.candidata = candidata
        self.nuevos_valores = nuevos_valores
        self.explicacion = ''

    def execute(self):
        for nuevo_valor in self.nuevos_valores:
            self.explicacion += f'\tEquiparar el atributo {nuevo_valor.atributo.nombre} = {nuevo_valor.valor}\n'
            
            for regla in self.candidata.reglas:
                if regla.atributo.nombre == nuevo_valor.atributo.nombre:
                    if not regla.execute(nuevo_valor):
                        return False, self.explicacion
        return True, self.explicacion

    
