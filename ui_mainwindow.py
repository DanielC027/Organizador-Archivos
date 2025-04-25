# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 626)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(140, 70, 741, 71))
        font = QFont()
        font.setPointSize(28)
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 390, 141, 71))
        font1 = QFont()
        font1.setFamily(u"Eras Medium ITC")
        font1.setPointSize(24)
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tabCambiarNombres = QWidget()
        self.tabCambiarNombres.setObjectName(u"tabCambiarNombres")
        self.groupBox_2 = QGroupBox(self.tabCambiarNombres)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 10, 581, 451))
        self.archivosSeleccionados_cambiarNombre_plainTextEdit = QPlainTextEdit(
            self.groupBox_2)
        self.archivosSeleccionados_cambiarNombre_plainTextEdit.setObjectName(
            u"archivosSeleccionados_cambiarNombre_plainTextEdit")
        self.archivosSeleccionados_cambiarNombre_plainTextEdit.setGeometry(
            QRect(10, 30, 221, 401))
        self.seleccionarArchivos_cambiarNombre_toolButton = QToolButton(
            self.groupBox_2)
        self.seleccionarArchivos_cambiarNombre_toolButton.setObjectName(
            u"seleccionarArchivos_cambiarNombre_toolButton")
        self.seleccionarArchivos_cambiarNombre_toolButton.setGeometry(
            QRect(490, 30, 25, 19))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 30, 131, 16))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 100, 181, 16))
        self.textoNuevoArchivos_cambiarNombre_lineEdit = QLineEdit(
            self.groupBox_2)
        self.textoNuevoArchivos_cambiarNombre_lineEdit.setObjectName(
            u"textoNuevoArchivos_cambiarNombre_lineEdit")
        self.textoNuevoArchivos_cambiarNombre_lineEdit.setGeometry(
            QRect(270, 120, 211, 20))
        self.cambiarNombres_pushButton = QPushButton(self.groupBox_2)
        self.cambiarNombres_pushButton.setObjectName(
            u"cambiarNombres_pushButton")
        self.cambiarNombres_pushButton.setGeometry(QRect(330, 240, 141, 41))
        self.tabWidget.addTab(self.tabCambiarNombres, "")
        self.tabMoverPorExtension = QWidget()
        self.tabMoverPorExtension.setObjectName(u"tabMoverPorExtension")
        self.groupBox = QGroupBox(self.tabMoverPorExtension)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 40, 531, 351))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.carpetaOrigen = QLineEdit(self.groupBox)
        self.carpetaOrigen.setObjectName(u"carpetaOrigen")

        self.gridLayout.addWidget(self.carpetaOrigen, 0, 1, 1, 1)

        self.origenBoton = QToolButton(self.groupBox)
        self.origenBoton.setObjectName(u"origenBoton")

        self.gridLayout.addWidget(self.origenBoton, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.carpetaDestino = QLineEdit(self.groupBox)
        self.carpetaDestino.setObjectName(u"carpetaDestino")

        self.gridLayout.addWidget(self.carpetaDestino, 1, 1, 1, 1)

        self.destinoBoton = QToolButton(self.groupBox)
        self.destinoBoton.setObjectName(u"destinoBoton")

        self.gridLayout.addWidget(self.destinoBoton, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.extensionArchivo = QLineEdit(self.groupBox)
        self.extensionArchivo.setObjectName(u"extensionArchivo")

        self.gridLayout.addWidget(self.extensionArchivo, 2, 1, 1, 2)

        self.moverArchivosBoton = QPushButton(self.groupBox)
        self.moverArchivosBoton.setObjectName(u"moverArchivosBoton")

        self.gridLayout.addWidget(self.moverArchivosBoton, 3, 0, 1, 3)

        self.tabWidget.addTab(self.tabMoverPorExtension, "")
        self.tabMoverPorNombres = QWidget()
        self.tabMoverPorNombres.setObjectName(u"tabMoverPorNombres")
        self.groupBox_3 = QGroupBox(self.tabMoverPorNombres)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(70, 40, 531, 351))
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.rutaOrigen_porNombre_lineEdit = QLineEdit(self.groupBox_3)
        self.rutaOrigen_porNombre_lineEdit.setObjectName(
            u"rutaOrigen_porNombre_lineEdit")

        self.gridLayout_2.addWidget(
            self.rutaOrigen_porNombre_lineEdit, 0, 1, 1, 1)

        self.rutaOrigen_porNombre_toolButton = QToolButton(self.groupBox_3)
        self.rutaOrigen_porNombre_toolButton.setObjectName(
            u"rutaOrigen_porNombre_toolButton")

        self.gridLayout_2.addWidget(
            self.rutaOrigen_porNombre_toolButton, 0, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.rutaDestino_porNombre_lineEdit = QLineEdit(self.groupBox_3)
        self.rutaDestino_porNombre_lineEdit.setObjectName(
            u"rutaDestino_porNombre_lineEdit")

        self.gridLayout_2.addWidget(
            self.rutaDestino_porNombre_lineEdit, 1, 1, 1, 1)

        self.rutaDestino_porNombre_toolButton_2 = QToolButton(self.groupBox_3)
        self.rutaDestino_porNombre_toolButton_2.setObjectName(
            u"rutaDestino_porNombre_toolButton_2")

        self.gridLayout_2.addWidget(
            self.rutaDestino_porNombre_toolButton_2, 1, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.nombreFiltrar_porNombre_lineEdit_3 = QLineEdit(self.groupBox_3)
        self.nombreFiltrar_porNombre_lineEdit_3.setObjectName(
            u"nombreFiltrar_porNombre_lineEdit_3")

        self.gridLayout_2.addWidget(
            self.nombreFiltrar_porNombre_lineEdit_3, 2, 1, 1, 2)

        self.moverPorNombre_pushButton = QPushButton(self.groupBox_3)
        self.moverPorNombre_pushButton.setObjectName(
            u"moverPorNombre_pushButton")

        self.gridLayout_2.addWidget(self.moverPorNombre_pushButton, 3, 0, 1, 3)

        self.tabWidget.addTab(self.tabMoverPorNombres, "")
        self.tabMoverSeleccionados = QWidget()
        self.tabMoverSeleccionados.setObjectName(u"tabMoverSeleccionados")
        self.groupBox_4 = QGroupBox(self.tabMoverSeleccionados)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(9, 9, 998, 523))
        self.mover_seleccionados_plainTextEdit = QPlainTextEdit(
            self.groupBox_4)
        self.mover_seleccionados_plainTextEdit.setObjectName(
            u"mover_seleccionados_plainTextEdit")
        self.mover_seleccionados_plainTextEdit.setGeometry(
            QRect(30, 50, 311, 431))
        self.mover_seleccionados_pushButton = QPushButton(self.groupBox_4)
        self.mover_seleccionados_pushButton.setObjectName(
            u"mover_seleccionados_pushButton")
        self.mover_seleccionados_pushButton.setGeometry(
            QRect(410, 280, 171, 61))
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(390, 180, 61, 16))
        self.nueva_ruta_mover_seleccionados_lineEdit = QLineEdit(
            self.groupBox_4)
        self.nueva_ruta_mover_seleccionados_lineEdit.setObjectName(
            u"nueva_ruta_mover_seleccionados_lineEdit")
        self.nueva_ruta_mover_seleccionados_lineEdit.setGeometry(
            QRect(470, 180, 181, 20))
        self.elegir_nueva_ruta_mover_seleccionados_toolButton = QToolButton(
            self.groupBox_4)
        self.elegir_nueva_ruta_mover_seleccionados_toolButton.setObjectName(
            u"elegir_nueva_ruta_mover_seleccionados_toolButton")
        self.elegir_nueva_ruta_mover_seleccionados_toolButton.setGeometry(
            QRect(660, 180, 25, 19))
        self.elegir_archivos_mover_seleccionados_toolButton_2 = QToolButton(
            self.groupBox_4)
        self.elegir_archivos_mover_seleccionados_toolButton_2.setObjectName(
            u"elegir_archivos_mover_seleccionados_toolButton_2")
        self.elegir_archivos_mover_seleccionados_toolButton_2.setGeometry(
            QRect(530, 80, 25, 19))
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(390, 80, 102, 16))
        self.tabWidget.addTab(self.tabMoverSeleccionados, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1040, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"ORGANIZADOR", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"ORGANIZADOR DE ARCHIVOS", None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"BY: DC", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), QCoreApplication.translate("MainWindow", u"ORGANIZADOR", None))
        self.groupBox_2.setTitle(QCoreApplication.translate(
            "MainWindow", u"Cambiar nombre de archivos seleccionados", None))
        self.seleccionarArchivos_cambiarNombre_toolButton.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Seleccionar archivos", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Texto que ira al prinicipio del archivo:", None))
        self.cambiarNombres_pushButton.setText(
            QCoreApplication.translate("MainWindow", u"CAMBIAR NOMBRES", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabCambiarNombres), QCoreApplication.translate("MainWindow", u"Cambiar Nombres", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "MainWindow", u"Mover de origen a destino por filtrado de extension", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Carpeta de origen: ", None))
        self.origenBoton.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Carpeta de destino:", None))
        self.destinoBoton.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Extensi\u00f3n del archivo:", None))
        self.moverArchivosBoton.setText(QCoreApplication.translate(
            "MainWindow", u"MOVER ARCHIVOS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabMoverPorExtension), QCoreApplication.translate("MainWindow", u"Mover Extension", None))
        self.groupBox_3.setTitle(QCoreApplication.translate(
            "MainWindow", u"Mover de origen a destino por filtrado de nombre", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Carpeta de origen: ", None))
        self.rutaOrigen_porNombre_toolButton.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Carpeta de destino:", None))
        self.rutaDestino_porNombre_toolButton_2.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Nombre a filtrar:", None))
        self.moverPorNombre_pushButton.setText(
            QCoreApplication.translate("MainWindow", u"MOVER ARCHIVOS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabMoverPorNombres), QCoreApplication.translate("MainWindow", u"Mover Nombre", None))
        self.groupBox_4.setTitle(QCoreApplication.translate(
            "MainWindow", u"Mover Seleccionados", None))
        self.mover_seleccionados_pushButton.setText(
            QCoreApplication.translate("MainWindow", u"MOVER SELECCIONADOS", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Nueva Ruta:", None))
        self.elegir_nueva_ruta_mover_seleccionados_toolButton.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.elegir_archivos_mover_seleccionados_toolButton_2.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Seleccionar Archivos:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabMoverSeleccionados), QCoreApplication.translate("MainWindow", u"Mover Seleccionados", None))
    # retranslateUi
