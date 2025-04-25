from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
import os


class MoverFiltrados(object):
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.origen_ruta = ""
        self.destino_ruta = ""
        self.extension_archivo = ""

        self.ui.origenBoton.clicked.connect(self.click_origen_boton)

        self.ui.destinoBoton.clicked.connect(self.click_destino_boton)

        self.ui.moverArchivosBoton.clicked.connect(
            self.click_cambiar_archivos_boton)

    @Slot()
    def click_origen_boton(self):
        """
        ORIGEN
        """
        print("boton origen")
        opciones = QFileDialog.Options()
        self.origen_ruta = QFileDialog.getExistingDirectory(
            self.ui.centralwidget, "Seleccionar carpeta", options=opciones)

        if self.origen_ruta:
            print("Carpeta seleccionada: ", self.origen_ruta)
            self.ui.carpetaOrigen.setText(self.origen_ruta)

    @Slot()
    def click_destino_boton(self):
        """
        DESTINO
        """
        print("boton destino")
        opciones = QFileDialog.Options()
        self.destino_ruta = QFileDialog.getExistingDirectory(
            self.ui.centralwidget, "Seleccionar carpeta", options=opciones)

        if self.destino_ruta:
            print("Carpeta seleccionada: ", self.destino_ruta)
            self.ui.carpetaDestino.setText(self.destino_ruta)

    @Slot()
    def click_cambiar_archivos_boton(self):
        """
        MOVER ARCHIVOS
        """
        print("cambiar archivos")

        if self.origen_ruta == "" or self.destino_ruta == "" or self.ui.extensionArchivo.text() == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Rutas no validas",
            )
        else:
            self.extension_archivo = self.ui.extensionArchivo.text()
            self.mover_archivos()

    def mover_archivos(self):
        """
        CAMBIAR DE UBICACION ARCHIVOS
        """
        try:
            archivos = os.listdir(self.origen_ruta)

            if archivos:
                for archivo in archivos:
                    if archivo.endswith(self.extension_archivo):
                        nvo_nombre = archivo
                        """
                        if " " in nvo_nombre:
                            nvo_nombre = archivo.replace(" ", "_")
                            old_name = self.origen_ruta + "/" + archivo
                            new_name = self.origen_ruta + "/" + nvo_nombre
                            os.system(f'ren "{old_name}" {new_name}')
                            print(f"ren {archivo} {nvo_nombre}")
                        """
                        vieja_ruta = self.origen_ruta + "/" + archivo
                        vieja_ruta = vieja_ruta.replace("/", "\\")
                        nueva_ruta = self.destino_ruta + "/" + archivo
                        nueva_ruta = nueva_ruta.replace("/", "\\")

                        os.system(f'move "{vieja_ruta}" "{nueva_ruta}"')
                        print(f"mv {vieja_ruta} {nueva_ruta}")

                QMessageBox.information(
                    self.ui.centralwidget,
                    "Exito",
                    "Se movieron los archivos con exito",
                )
            else:
                QMessageBox.information(
                    self.ui.centralwidget,
                    "Advertencia",
                    "No se encontraron archivos",
                )
        except:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No se pudo completar la acción",
            )
