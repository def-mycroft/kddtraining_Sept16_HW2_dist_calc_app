""" Distance calculator widget"""
import sys
from PyQt5.QtWidgets import QApplication
import model
import view


def display_distance(widget):
    """ Gets the distance from get_distance and displays in view"""

    distance_value = get_distance(widget) # Get distance from model.
    distance_display = 'The distance is: %s miles.' % distance_value
    widget.status_bar.showMessage(distance_display)


def get_distance(widget):
    """ Takes locations from view and returns distance"""

    # Get origin / destination user input from the view.
    origin_location = widget.origin_input.text()
    destination_location = widget.destination_input.text()

    # Return value is from the model module get_distance function.
    return int(model.get_distance(origin_location, destination_location) / 1609.34)


def display_window():
    """ Displays the window and allow for use."""

    application = QApplication(sys.argv) # I don't understand what this does.
    my_widget = view.MainWindow() # Instantiate an instance of the window.

    def pass_distance_display():
        """ Passes the widget object to the display_distance function"""
        display_distance(my_widget)

    # Signal to calculate distance.
    my_widget.button_calculate.clicked.connect(pass_distance_display)

    sys.exit(application.exec_()) # I don't understand what this does.
