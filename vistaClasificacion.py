#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Antonio Javier Quintero García y Noelia Ruiz Morón
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFrame, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QPlainTextEdit, QTableWidget, QTableWidgetItem, QComboBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


from bcClasificacion import *
import controladorClasificacion as ctrl
import aeronavesClasificacion as bc_aeronaves
import alimentosClasificacion as bc_alimentos
from aeronavesClasificacion import Aeronave, clases

class ClasificadorDlg(QWidget):
    def __init__(self):        
        super(ClasificadorDlg, self).__init__()
        
        # Atributos de propósito general
        self.aeronaveGenerica = bc_aeronaves.Aeronave()
        self.alimentoGenerico = bc_alimentos.Alimento()
        self.dominio = 'Aeronaves'
        
        
        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        
        # Crear objetos genéricos después de definir la interfaz
        self.generarObjetosGenericos()
        self.crearInterfazUsuario()
        
        
        # Obtener la geometría de la pantalla
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()

        # Calcular la posición inicial para centrar la ventana en la pantalla
        x = int((screen_geometry.width() - 1200) / 2)
        y = int((screen_geometry.height() - 600) / 2)

        # Establecer la geometría de la ventana
        self.setGeometry(x, y, 1200, 600)
        self.setWindowTitle(u"TAREA DE CLASIFICACIÓN")
        self.show()
        
        # Señales
        self.listWidgetClasesCandidatas.itemClicked.connect(self.mostrarInformacionClase)
        self.listWidgetClasesPosibles.itemClicked.connect(self.mostrarInformacionClase)
        self.comboBoxDominio.currentIndexChanged.connect(self.actualizarDominio)
        self.clasificarButton.clicked.connect(self.clasificar)
        self.borrarButton.clicked.connect(self.borrarInterfaz)
        self.salirButton.clicked.connect(self.close)

    def generarObjetosGenericos(self):
        # Generación de un objeto representante del dominio de las aeronaves
        caracteristicasAeronave = []
        for atributo in self.aeronaveGenerica.atributos:
            caracteristicasAeronave.append(Caracteristica(atributo, None))  
        self.aeronave = Objeto('Aeronave', caracteristicasAeronave)

        # Generación de un objeto representante del dominio de los alimentos
        caracteristicasAlimentos = []
        for atributo in self.alimentoGenerico.atributos:
            caracteristicasAlimentos.append(Caracteristica(atributo, None))
        self.alimento = Objeto('Alimento', caracteristicasAlimentos)

    def crearInterfazUsuario(self):
        self.etiquetasHeader = ['ATRIBUTO', 'VALOR']
        
        # Crear la tabla del dominio de aeronaves
        self.tablaWidgetAeronave = QTableWidget(len(self.aeronaveGenerica.atributos), 2)
        self.tablaWidgetAeronave.setColumnWidth(0, 283)
        self.tablaWidgetAeronave.setColumnWidth(1, 283)
        self.tablaWidgetAeronave.setHorizontalHeaderLabels(self.etiquetasHeader)
        self.tablaWidgetAeronave.verticalHeader().setVisible(False)
        
        for i in range(len(self.aeronaveGenerica.atributos)):
            label = QTableWidgetItem(self.aeronaveGenerica.atributos[i].nombre)
            label.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.tablaWidgetAeronave.setItem(i, 0, label)
            
            if self.aeronaveGenerica.atributos[i].tipo == 'multiple':
                widget = QComboBox()
                for posibleValor in self.aeronaveGenerica.atributos[i].posiblesValores:
                    if posibleValor is not str:
                        widget.addItem(str(posibleValor))
                    else:
                        widget.addItem(posibleValor)
                self.tablaWidgetAeronave.setCellWidget(i, 1, widget)
            else:
                widget = QTableWidgetItem('')
                self.tablaWidgetAeronave.setItem(i, 1, widget)
        
        # Crear la tabla del dominio de alimentos
        self.tablaWidgetAlimento = QTableWidget(len(self.alimentoGenerico.atributos), 2)
        self.tablaWidgetAlimento.setColumnWidth(0, 283)
        self.tablaWidgetAlimento.setColumnWidth(1, 283)
        self.tablaWidgetAlimento.setHorizontalHeaderLabels(self.etiquetasHeader)
        self.tablaWidgetAlimento.verticalHeader().setVisible(False)
        
        for i in range(len(self.alimentoGenerico.atributos)):
            label = QTableWidgetItem(self.alimentoGenerico.atributos[i].nombre)
            label.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.tablaWidgetAlimento.setItem(i, 0, label)
            
            if self.alimentoGenerico.atributos[i].tipo == 'multiple':
                widget = QComboBox()
                for posibleValor in self.alimentoGenerico.atributos[i].posiblesValores:
                    if posibleValor is not str:
                        widget.addItem(str(posibleValor))
                    else:
                        widget.addItem(posibleValor)
                self.tablaWidgetAlimento.setCellWidget(i, 1, widget)
            else:
                widget = QTableWidgetItem('')
                self.tablaWidgetAlimento.setItem(i, 1, widget)
        
        # Botones y texto
        self.clasificarButton = QPushButton("Clasificar")
        self.borrarButton = QPushButton("Borrar")
        self.borrarButton.setIcon(QIcon(f"fotos/borrar.jpg"))
        self.salirButton = QPushButton("Salir")
        self.salirButton.setIcon(QIcon(f"fotos/salir.jpg"))
        
        self.listWidgetClasesCandidatas = QListWidget()
        self.plainTextEditDescripcionClases = QPlainTextEdit()
        self.plainTextEditExplicacion = QPlainTextEdit()   
        
        #Estilo de los botones  
        self.clasificarButton.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; padding: 5px 10px; font-size: 12px;")
        self.borrarButton.setStyleSheet("background-color: #f44336; color: white; border-radius: 5px; padding: 5px 10px; font-size: 12px;")
        self.salirButton.setStyleSheet("background-color: #555555; color: white; border-radius: 5px; padding: 5px 10px; font-size: 12px;")
            
        #Tamaño de los botones
        self.clasificarButton.setFixedWidth(80)
        self.borrarButton.setFixedWidth(80)
        self.salirButton.setFixedWidth(80)

        # Configurar políticas de expansión
        self.plainTextEditDescripcionClases.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.plainTextEditExplicacion.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
           
        
        self.listWidgetClasesSeleccionadas = QListWidget()
        self.plainTextEditDescripcionClases = QPlainTextEdit()
        self.plainTextEditExplicacion = QPlainTextEdit()
        self.plainTextEditExplicacion.setMinimumWidth(350)

    
        # ComboBox para seleccionar el dominio
        self.comboBoxDominio = QComboBox()
        self.comboBoxDominio.addItems(['Aeronaves', 'Alimentos'])
        self.comboBoxDominio.setCurrentIndex(0)
        self.comboBoxDominio.setFixedWidth(100)
     
        # Nueva QListWidget para las Clases Posibles
        self.listWidgetClasesPosibles = QListWidget()

        # QLabel para mostrar la imagen de la clase seleccionada
        self.imagenClaseCandidata = QLabel(self)
        self.imagenClaseCandidata.setFixedSize(200, 200)
        self.imagenClaseCandidata.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenClaseCandidata.setStyleSheet("margin-left: 10px")

        # QFrame para contener la imagen
        self.imagenFrame = QFrame(self)
        self.imagenFrame.setFrameShape(QFrame.Box)
        self.imagenFrame.setFrameShadow(QFrame.Plain)
        self.imagenFrame.setLineWidth(2)
        self.imagenFrame.setFixedSize(210, 204)  # Mantenemos el tamaño fijo en la dirección vertical
        self.imagenFrame.setStyleSheet("background-color: white;")

        # Layout para centrar la imagen dentro del frame y permitir la expansión horizontal
        imagenLayout = QHBoxLayout(self.imagenFrame)
        imagenLayout.addWidget(self.imagenClaseCandidata)
        imagenLayout.setAlignment(QtCore.Qt.AlignCenter)  # Centramos la imagen horizontalmente
        imagenLayout.setContentsMargins(3, 3, 3, 3)  # Agregamos un pequeño margen alrededor de la imagen
        self.imagenFrame.setLayout(imagenLayout)

        # Añadir el QFrame al layout principal
        self.grid.addWidget(self.listWidgetClasesCandidatas, 2, 1)
        self.grid.addWidget(self.imagenFrame, 2, 2, 1, 2)
        
        # Crear un layout horizontal para agrupar la etiqueta y el ComboBox
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(QLabel("Dominio:"))
        layout_horizontal.addWidget(self.comboBoxDominio)


        # Alinea el layout de los widgets en el centro
        layout_horizontal.setAlignment(Qt.AlignCenter)

        # Crear un contenedor para el layout horizontal
        contenedor_dominio = QWidget()
        contenedor_dominio.setLayout(layout_horizontal)

        # Agregar el contenedor a la celda (0, 0) de la cuadrícula
        self.grid.addWidget(contenedor_dominio, 0, 0, 1, 3)
  
        
        label_informacion_objeto = QLabel("Información del objeto a clasificar:")
        label_informacion_objeto.setStyleSheet("font-size: 12px; font-weight: bold; color: #333333; background-color: #f0f0f0; border-radius: 5px;")
        self.grid.addWidget(label_informacion_objeto, 1, 0)
        
               
        label_clases_candidatas = QLabel("Clases candidatas:")
        label_clases_candidatas.setStyleSheet("font-size: 12px; font-weight: bold; color: #333333; background-color: #f0f0f0; border-radius: 5px;")
        self.grid.addWidget(label_clases_candidatas, 1, 1)
        
        
        self.grid.addWidget(self.tablaWidgetAeronave, 2, 0)
        self.tablaWidgetAeronave.setMinimumWidth(568)
        
        self.grid.addWidget(self.tablaWidgetAlimento, 2, 0)
        self.tablaWidgetAlimento.setMinimumWidth(568)


        # Crear QLabel para "Reglas de la Clase"
        label_descripcion = QLabel("Reglas de la clase:")
        label_descripcion.setStyleSheet("font-size: 12px; font-weight: bold; color: #333333; background-color: #f0f0f0; border-radius: 5px;")
        self.grid.addWidget(label_descripcion, 3, 0)
        
        
        label_explicacion = QLabel("Explicación de la clasificación:")
        label_explicacion.setStyleSheet("font-size: 12px; font-weight: bold; color: #333333; background-color: #f0f0f0; border-radius: 5px;")
        self.grid.addWidget(label_explicacion, 3, 1)
       
      
        self.grid.addWidget(self.plainTextEditDescripcionClases, 4, 0)
        self.grid.addWidget(self.plainTextEditExplicacion, 4, 1)

        # Añadir QLabel para la imagen de la clase seleccionada
        self.grid.addWidget(self.listWidgetClasesCandidatas, 2, 1)
        self.grid.addWidget(self.imagenClaseCandidata, 2, 2, 1, 2)
        self.imagenClaseCandidata.setAlignment(QtCore.Qt.AlignCenter)
          
               
        label_clases_seleccionadas = QLabel("Clases seleccionadas:")
        label_clases_seleccionadas.setStyleSheet("font-size: 12px; font-weight: bold; color: #333333; background-color: #f0f0f0; border-radius: 5px;")
        self.grid.addWidget(label_clases_seleccionadas, 3, 2)
          

        self.grid.addWidget(self.listWidgetClasesPosibles, 4, 2)
        self.listWidgetClasesPosibles.setMaximumWidth(210)

        # Crear un nuevo contenedor para los botones
        contenedor_botones = QWidget()

        # Crear un layout horizontal para los botones
        layout_botones = QHBoxLayout(contenedor_botones)
        layout_botones.addWidget(self.clasificarButton)
        layout_botones.addWidget(self.borrarButton)
        layout_botones.addWidget(self.salirButton)
        layout_botones.setContentsMargins(0, 0, 0, 0)
        layout_botones.setSpacing(10)

        # Alinea el layout de los botones en el centro
        layout_botones.setAlignment(Qt.AlignCenter)

        # Agregar el contenedor de botones a la fila 5 de la cuadrícula
        self.grid.addWidget(contenedor_botones, 5, 0, 1, 3)

        # Establecer el diseño en la ventana principal
        self.setLayout(self.grid)

        # Actualizar la interfaz según el dominio inicial
        self.actualizarInterfazSegunDominio()        
        
        #Modificar estilo de las cabeceras de la tabla:
        self.tablaWidgetAeronave.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #cccccc; }")
        self.tablaWidgetAlimento.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #cccccc; }")


    def actualizarInterfazSegunDominio(self):
        if self.dominio == 'Aeronaves':
            self.tablaWidgetAlimento.hide()
            self.tablaWidgetAeronave.show()
        else:
            self.tablaWidgetAeronave.hide()
            self.tablaWidgetAlimento.show()
        
        self.actualizarClasesCandidatasWidget()
        self.plainTextEditDescripcionClases.clear()
        self.listWidgetClasesSeleccionadas.clear()
        self.plainTextEditExplicacion.clear()
        self.listWidgetClasesPosibles.clear()
        self.imagenClaseCandidata.clear()

    def obtenerInformacionObjeto(self):
        informacionCorrecta = True
        if self.dominio == "Aeronaves":
            for i in range(self.tablaWidgetAeronave.rowCount()):
                if self.aeronave.caracteristicas[i].atributo.tipo == 'str':
                    self.aeronave.caracteristicas[i].valor = self.tablaWidgetAeronave.item(i, 1).text()
                elif self.aeronave.caracteristicas[i].atributo.tipo == 'int':
                    try:
                        self.aeronave.caracteristicas[i].valor = int(self.tablaWidgetAeronave.item(i, 1).text())
                        self.tablaWidgetAeronave.item(i, 1).setBackground(QtGui.QColor(255, 255, 255))
                    except ValueError:
                        self.tablaWidgetAeronave.item(i, 1).setBackground(QtGui.QColor(255, 0, 0))
                        informacionCorrecta = False
                elif self.aeronave.caracteristicas[i].atributo.tipo == 'float':
                    try:
                        self.aeronave.caracteristicas[i].valor = float(self.tablaWidgetAeronave.item(i, 1).text())
                        self.tablaWidgetAeronave.item(i, 1).setBackground(QtGui.QColor(255, 255, 255))
                    except ValueError:
                        self.tablaWidgetAeronave.item(i, 1).setBackground(QtGui.QColor(255, 0, 0))
                        informacionCorrecta = False
                elif self.aeronave.caracteristicas[i].atributo.tipo == 'multiple':         
                    self.aeronave.caracteristicas[i].valor = self.tablaWidgetAeronave.cellWidget(i, 1).currentText()                         
            self.aeronave.describeObjeto()
            
            
        elif self.dominio == "Alimentos":
            for i in range(self.tablaWidgetAlimento.rowCount()):
                if self.alimento.caracteristicas[i].atributo.tipo == 'str':
                    self.alimento.caracteristicas[i].valor = self.tablaWidgetAlimento.item(i, 1).text()
                elif self.alimento.caracteristicas[i].atributo.tipo == 'int':
                    try:
                        self.alimento.caracteristicas[i].valor = int(self.tablaWidgetAlimento.item(i, 1).text())
                        self.tablaWidgetAlimento.item(i, 1).setBackground(QtGui.QColor(255, 255, 255))
                    except ValueError:
                        self.tablaWidgetAlimento.item(i, 1).setBackground(QtGui.QColor(255, 0, 0))
                        informacionCorrecta = False
                elif self.alimento.caracteristicas[i].atributo.tipo == 'float':
                    try:
                        self.alimento.caracteristicas[i].valor = float(self.tablaWidgetAlimento.item(i, 1).text())
                        self.tablaWidgetAlimento.item(i, 1).setBackground(QtGui.QColor(255, 255, 255))
                    except ValueError:
                        self.tablaWidgetAlimento.item(i, 1).setBackground(QtGui.QColor(255, 0, 0))
                        informacionCorrecta = False
                elif self.alimento.caracteristicas[i].atributo.tipo == 'multiple':
                    self.alimento.caracteristicas[i].valor = self.tablaWidgetAlimento.cellWidget(i, 1).currentText()                          
            self.alimento.describeObjeto()
        return informacionCorrecta

    def actualizarClasesCandidatasWidget(self):        
        # Obtener listado de clases candidatas
        if self.dominio == 'Aeronaves':
            self.cc = bc_aeronaves.clases()
        else:
            self.cc = bc_alimentos.clases()            
        
        # Crear listado de clases candidatas
        if self.cc is not None:
            stringList = [c.nombre for c in self.cc if hasattr(c, 'nombre') and isinstance(c.nombre, str)]
            
            # Comprobar si hay que vaciar el listado
            if self.listWidgetClasesCandidatas.count() > 0:
                self.listWidgetClasesCandidatas.clear()
            
            # Añadir las clases candidatas al listado    
            self.listWidgetClasesCandidatas.addItems(stringList)
            self.listWidgetClasesCandidatas.setCurrentRow(0)
            
            # Actualizar también las clases posibles
            self.listWidgetClasesPosibles.clear()
            self.listWidgetClasesPosibles.addItems(stringList)
            self.listWidgetClasesPosibles.setCurrentRow(0)


    def mostrarInformacionClase(self, item):
      nombreClase = item.text()
      for clase in self.cc:
        if clase.nombre == nombreClase:
            self.plainTextEditDescripcionClases.clear()
            self.plainTextEditDescripcionClases.appendPlainText(clase.descripcion())
            self.mostrarImagenClase(clase.nombre)
            break
          
    def mostrarImagenClase(self, nombreClase):
     try:
        # Ruta de la imagen
        rutaImagen = f"fotos/{nombreClase}.jpg"

        # Calcula el ancho y alto disponibles para la imagen
        ancho_disponible = self.imagenClaseCandidata.width()
        alto_disponible = self.imagenClaseCandidata.height()

        # Cargar la imagen usando QPixmap
        pixmap = QtGui.QPixmap(rutaImagen)

        # Redimensionar la imagen para que ocupe el ancho y alto disponibles
        pixmap = pixmap.scaled(ancho_disponible, alto_disponible, QtCore.Qt.KeepAspectRatio)

        # Establecer el QPixmap escalado como contenido de la imagen del QLabel
        self.imagenClaseCandidata.setPixmap(pixmap)

        # Centrar la imagen horizontal y verticalmente dentro del QLabel
        self.imagenClaseCandidata.setAlignment(QtCore.Qt.AlignCenter)
     except Exception as e:
        # Borrar el QLabel si la imagen no se encuentra o si ocurre algún error
        self.imagenClaseCandidata.clear()



    def clasificar(self):
        if self.obtenerInformacionObjeto():
            # Obtener clases candidatas y explicación del controlador
            if self.dominio == 'Aeronaves':
                resultado, explicacion = ctrl.eventoClasificar(self.aeronave, self.dominio)
            elif self.dominio == 'Alimentos':
                resultado, explicacion = ctrl.eventoClasificar(self.alimento, self.dominio)

            # Actualizar el texto de justificación en la interfaz
            self.plainTextEditExplicacion.clear()
            self.plainTextEditExplicacion.appendPlainText(explicacion)
            self.plainTextEditExplicacion.moveCursor(QtGui.QTextCursor.Start)

            if resultado:
                # Obtener nombres de clases seleccionadas
                clases_seleccionadas = [clase.nombre for clase in resultado]

                # Mostrar las clases seleccionadas
                self.listWidgetClasesSeleccionadas.clear()
                self.listWidgetClasesSeleccionadas.addItems(clases_seleccionadas)

                # Obtener nombres de clases posibles
                clases_posibles = [c.nombre for c in self.cc if c.nombre not in clases_seleccionadas]

                # Actualizar las clases posibles con las clases seleccionadas
                self.listWidgetClasesPosibles.clear()
                self.listWidgetClasesPosibles.addItems(clases_seleccionadas) 

                # Si la lista de clases posibles está vacía, mostrar un mensaje
                if not clases_posibles:
                    self.listWidgetClasesPosibles.addItem("No hay clases posibles")

    def borrarInterfaz(self):
        self.listWidgetClasesSeleccionadas.clear()
        self.plainTextEditExplicacion.clear()
        self.listWidgetClasesPosibles.clear()
        self.imagenClaseCandidata.clear()
        self.plainTextEditDescripcionClases.clear()
        
        # Limpiar valores de la tabla de aeronaves
        for i in range(self.tablaWidgetAeronave.rowCount()):
         if self.tablaWidgetAeronave.cellWidget(i, 1) is not None:
            self.tablaWidgetAeronave.cellWidget(i, 1).setCurrentIndex(0)
         else:
            self.tablaWidgetAeronave.item(i, 1).setText('')
   
        # Limpiar valores de la tabla de alimentos
        for i in range(self.tablaWidgetAlimento.rowCount()):
         if self.tablaWidgetAlimento.cellWidget(i, 1) is not None:
            self.tablaWidgetAlimento.cellWidget(i, 1).setCurrentIndex(0)
         else:
            self.tablaWidgetAlimento.item(i, 1).setText('')

    def actualizarDominio(self, index):
        if index == 0:
            self.dominio = 'Aeronaves'
        elif index == 1:
            self.dominio = 'Alimentos'
        self.actualizarInterfazSegunDominio()

# Función principal para ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ClasificadorDlg()
    sys.exit(app.exec_())
