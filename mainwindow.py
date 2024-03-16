from ui_parametric_propeller import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from foil_load import DatFileLister
from PySide6 import QtGui
from model import Model

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Set window name
        self.setWindowTitle("Parametric propeller design")
        self.setWindowIcon(QtGui.QIcon('./img/icon.ico'))
        self.generate_button.clicked.connect(self.do_something)
        # Disable vortex gen button // NOT IMPLEMENTED //
        self.vortex_gen_checkbox.setEnabled(False)
        self.preview_button.setEnabled(False)
        # Populate the names of airfoils in list without .dat extension
        folder_path = './foils'
        global dat_lister
        dat_lister = DatFileLister(folder_path)
        self.blade_type_list.addItems(dat_lister.list_dat_files())
    def do_something(self):
        model = Model(
            blade_type=dat_lister.read_dat_file(self.blade_type_list.currentText()),
            num_blade_input=self.num_blade_input.value(),
            attack_angle_input=self.attack_angle_input.value(),
            hub_diameter_input=self.hub_diameter_input.value(),
            out_diameter_input=self.out_diameter_input.value(),
            height_input=self.height_input.value()
        )
        model.model()