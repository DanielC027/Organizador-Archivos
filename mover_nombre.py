from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
import os


class MoverNombre(object):
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.origen_ruta = ""
        self.destino_ruta = ""
        self.nombre_filtrar = ""

        self.ui.rutaOrigen_porNombre_toolButton.clicked.connect(
            self.click_origen_boton)

        self.ui.rutaDestino_porNombre_toolButton_2.clicked.connect(
            self.click_destino_boton)

        self.ui.moverPorNombre_pushButton.clicked.connect(
            self.click_cambiar_archivos_boton)

    @Slot()
    def click_origen_boton(self):
        """
        ORIGEN
        """

        opciones = QFileDialog.Options()
        self.origen_ruta = QFileDialog.getExistingDirectory(
            self.ui.centralwidget, "Seleccionar carpeta", options=opciones)

        if self.origen_ruta:
            print("Carpeta seleccionada: ", self.origen_ruta)
            self.ui.rutaOrigen_porNombre_lineEdit.setText(self.origen_ruta)

    @Slot()
    def click_destino_boton(self):
        """
        DESTINO
        """
        print("destomp")
        opciones = QFileDialog.Options()
        self.destino_ruta = QFileDialog.getExistingDirectory(
            self.ui.centralwidget, "Seleccionar carpeta", options=opciones)

        if self.destino_ruta:
            print("Carpeta seleccionada: ", self.destino_ruta)
            self.ui.rutaDestino_porNombre_lineEdit.setText(self.destino_ruta)

    @Slot()
    def click_cambiar_archivos_boton(self):
        """
        MOVER ARCHIVOS
        """

        if self.origen_ruta == "" or self.destino_ruta == "" or self.ui.nombreFiltrar_porNombre_lineEdit_3.text() == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Rutas no validas",
            )
        else:
            self.nombre_filtrar = self.ui.nombreFiltrar_porNombre_lineEdit_3.text()
            self.mover_archivos()

    def mover_archivos(self):
        """
        CAMBIAR DE UBICACION ARCHIVOS
        """
        try:
            archivos = os.listdir(self.origen_ruta)

            if archivos:
                for archivo in archivos:
                    if self.nombre_filtrar in archivo:
                        print(
                            f"archivo {archivo} nombre: {self.nombre_filtrar}")
                        vieja_ruta = self.origen_ruta + '/' + archivo
                        vieja_ruta = vieja_ruta.replace("/", "\\")
                        nueva_ruta = self.destino_ruta + '/' + archivo
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
