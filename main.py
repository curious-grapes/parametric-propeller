import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import ctypes

myappid = 'curious-grapes.parametric-propeller.designer.0.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

# pyinstaller main.spec --noconfirm
# pyside6-rcc -o new_rc.py new.qrc
