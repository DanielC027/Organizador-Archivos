from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
import os


class CambiarNombre(object):
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.nuevo_texto = ""
        self.lista_nombres = []

        self.ui.seleccionarArchivos_cambiarNombre_toolButton.clicked.connect(
            self.seleccionar_archivos)

        self.ui.cambiarNombres_pushButton.clicked.connect(
            self.click_cambiar_nombres)

    @Slot()
    def seleccionar_archivos(self):
        """
        ORIGEN
        """
        print("si")
        opciones = QFileDialog.Options()
        self.archivos = QFileDialog.getOpenFileNames(
            self.ui.centralwidget, "Seleccionar archivos", options=opciones)

        if self.archivos:
            nueva_lista = []
            self.lista_archivos = tuple(
                x for x in self.archivos if x != 'All Files (*)')

            print("Archivos seleccionados:", self.lista_archivos)
            lista_texto = ""
            for archivo in self.lista_archivos:
                for nombre in archivo:
                    print(nombre)
                    texto = nombre.split("/")[-1]
                    lista_texto = lista_texto + texto + "\n"
                    nueva_lista.append(nombre)

            print(nueva_lista)
            self.lista_nombres = nueva_lista
            self.ui.archivosSeleccionados_cambiarNombre_plainTextEdit.setPlainText(
                lista_texto)

    @Slot()
    def click_cambiar_nombres(self):
        """
        CAMBIAR NOMBRES
        """
        if self.lista_nombres is False:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Falta de información",
            )
        else:
            self.cambiar_nombres()

    @Slot()
    def cambiar_nombres(self):
        """
        CAMBIAR DE UBICACION ARCHIVOS
        """
        try:
            print(self.lista_nombres)

            for nombre in self.lista_nombres:
                print(nombre)

                directorio, nombre_arch = os.path.split(nombre)

                nvo_texto = self.ui.textoNuevoArchivos_cambiarNombre_lineEdit.text() + \
                    nombre_arch

                nombre = nombre.replace("/", "\\")
                os.system(f'ren "{nombre}" "{nvo_texto}"')

            QMessageBox.information(
                self.ui.centralwidget,
                "Exito",
                "Se agrego la cadena de texto",
            )

        except:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No se pudo completar la acción",
            )
