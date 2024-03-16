import sys
import numpy as np

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# Assuming you have the 'points' list from your airfoil
# (Replace this with your actual airfoil data)
# points = [
#     (1.000000, 0.002000),
#     # ... (rest of your airfoil points)
# ]

class FoilGraph(QWidget):
    def __init__(self, points, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        global canvas
        canvas = FigureCanvas(Figure(figsize=(300/80, 146/80)))
        # layout.addWidget(NavigationToolbar(canvas, self))
        layout.addWidget(canvas)
        self.points = points
        self.ax = canvas.figure.subplots()
        self.plot_airfoil()
        
        canvas.figure.subplots_adjust(
            top=1.0,
            bottom=0.195,
            left=0.125,
            right=0.9,
            hspace=0.2,
            wspace=0.2
        )
        

    def plot_airfoil(self):
        points = self.points
        x, y = zip(*points)  # Unpack x and y coordinates from the airfoil points
        self.ax.plot(x, y, label='')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.grid(True)
        self.ax.set_title('Airfoil Shape')
        self.ax.set_aspect('equal', adjustable='box')  # Optional: Set aspect ratio to equal
        canvas.draw()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_plot_size()

    def update_plot_size(self):

        width, height = canvas.width(), canvas.height()
        canvas.figure.set_size_inches(width / canvas.figure.dpi, height / canvas.figure.dpi)
        canvas.draw()

if __name__ == "__main__":
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    main_window = QMainWindow()
    foil_graph = FoilGraph(main_window)
    main_window.setCentralWidget(foil_graph)
    main_window.show()

    sys.exit(qapp.exec())
