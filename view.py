"""View for Distance Calculator"""
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGridLayout,
                             QPushButton, QStatusBar)


class MainWindow(QWidget):
    """ The window widget for the distance calculator"""
    def __init__(self):
        super().__init__()
        self.initialize_ui()


    def initialize_ui(self):
        """ The window widget"""

        # To and From labels for input boxes.
        origin_label = QLabel('From')
        destination_label = QLabel('To')

        # Status bar displays the output.
        self.status_bar = QStatusBar()

        # Input boxes.
        self.origin_input = QLineEdit(self)
        self.destination_input = QLineEdit(self)

        # Calculate button.
        self.button_calculate = QPushButton('Get Distance!!', self)

        # Sets grid spacing and layout.
        grid = QGridLayout()
        grid.setSpacing(10)

        # Adding widgets to layout.
        grid.addWidget(origin_label, 0, 0)
        grid.addWidget(self.origin_input, 0, 1)
        grid.addWidget(destination_label, 1, 0)
        grid.addWidget(self.destination_input, 1, 1)
        grid.addWidget(self.button_calculate, 2, 1)
        grid.addWidget(self.status_bar, 2, 2)

        # Set the layout.
        self.setLayout(grid)

        # Set window size and dimensions.
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Distance Calculator')
        self.show()
