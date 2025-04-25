
from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow

from cambiar_nombre import CambiarNombre
from mover_filtrados import MoverFiltrados
from mover_nombre import MoverNombre
from mover_seleccionados import MoverSeleccionados


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cambiar_nombres = CambiarNombre(self.ui)
        self.mover_filtrados = MoverFiltrados(self.ui)
        self.mover_nombre = MoverNombre(self.ui)
        self.mover_seleccionados = MoverSeleccionados(self.ui)
