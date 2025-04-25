from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
import os


class MoverSeleccionados(object):
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.nuevo_texto = ""
        self.nueva_ruta = ""
        self.lista_nombres = []

        self.ui.elegir_archivos_mover_seleccionados_toolButton_2.clicked.connect(
            self.seleccionar_archivos)

        self.ui.elegir_nueva_ruta_mover_seleccionados_toolButton.clicked.connect(
            self.poner_nueva_ruta)

        self.ui.mover_seleccionados_pushButton.clicked.connect(
            self.mover_seleccionados)

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
            self.ui.mover_seleccionados_plainTextEdit.setPlainText(
                lista_texto)

    @Slot()
    def mover_seleccionados(self):
        """
        CAMBIAR NOMBRES
        """
        if self.lista_nombres is False and self.nueva_ruta == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Falta de información",
            )
        else:
            self.mover_a_nueva_ruta()

    @Slot()
    def mover_a_nueva_ruta(self):
        """
        CAMBIAR DE UBICACION ARCHIVOS
        """
        try:
            print(self.lista_nombres)

            for nombre in self.lista_nombres:
                print(nombre)

                nombre = nombre.replace("/", "\\")
                directorio, nombre_arch = os.path.split(nombre)
                nueva_ruta = os.path.join(self.nueva_ruta, nombre_arch)
                nueva_ruta = nueva_ruta.replace("/", "\\")

                os.system(f'move "{nombre}" "{nueva_ruta}"')

            QMessageBox.information(
                self.ui.centralwidget,
                "Exito",
                "Se movieron los archivos",
            )

        except:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No se pudo completar la acción",
            )

    def poner_nueva_ruta(self):
        """
        poner nueva ruta
        """
        print("poner ruta mover selecciondps")
        opciones = QFileDialog.Options()
        destino_ruta = QFileDialog.getExistingDirectory(
            self.ui.centralwidget, "Seleccionar carpeta", options=opciones)

        if destino_ruta:
            print("Carpeta seleccionada: ", destino_ruta)
            self.nueva_ruta = destino_ruta
            self.ui.nueva_ruta_mover_seleccionados_lineEdit.setText(
                destino_ruta)
