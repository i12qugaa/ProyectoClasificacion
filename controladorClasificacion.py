#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Antonio Javier Quintero García y Noelia Ruiz Morón
"""

from modeloClasificacion import MetodoPoda

def eventoClasificar(objeto, dominio):
    # Crear una instancia del Método de Poda y ejecutarlo
    mp = MetodoPoda(objeto, dominio)
    clases_candidatas, explicacion = mp.execute()

    return clases_candidatas, explicacion

