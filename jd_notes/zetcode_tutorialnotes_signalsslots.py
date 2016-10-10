"""
http://zetcode.com/gui/pyqt5/eventssignals/

Events
All GUI applications are event-driven.
Events are generated mainly by the user of an application, but can be
by other means as well.
When the exec_() method is called on the application, the application
enters the main loop. The main loop fetches events and sends them to objects.

There are three participants in the event model:
event source - the object whose state changes - generates events.
event object - encapsulates the state changes into event source.
event target - object that wants to be notified.

PyQt5 uses signals and slots to handle events - communication between
objects.
a signal is emitted when an event occurs, a slot is any python callable.

"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
        QVBoxLayout, QApplication)


class slider_window(QWidget):

    def __init__(self):
        """ What does this do?""" # TODO
        super().__init__()

        self.initUI()

    def initUI(self):

        number_thing = QLCDNumber(self)
        slider_thing = QSlider(Qt.Horizontal, self)

        # I guess this creates the actual box?
        box_thing = QVBoxLayout()
        # And these things would add the number and slider widget to
        # the box.
        box_thing.addWidget(number_thing)
        box_thing.addWidget(slider_thing)

        # I don't know what this does # TODO
        # this is a method that is being called on self.
        # I disabeled this thing and nothing happened, so I don't know what
        # it does.
        self.setLayout(box_thing)

        # Here is where the connection is actually happening.
        slider_thing.valueChanged.connect(number_thing)

        # Sets the window size, I'm assuming.
        self.setGeometry(300, 300, 250, 150)
        # Sets the window title.
        self.setWindowTitle('Signal and Slot')
        # Displays the window.
        self.show()


if __name__ == '__main__':

    application = QApplication(sys.argv)
    my_widget_instance = slider_window()
    sys.exit(app.exec_())




















