"""

Taking notes on tutorial from website:
    http://zetcode.com/gui/pyqt5/firstprograms/

"""
# Necessary imports from the PyQt5.QtWidgets module.
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # Every PyQt5 application must create an application object.
    # The sys.arge parameter is a list of arguments from a command line.
    # This is a way to control the startup of the script.
    application_object = QApplication(sys.argv)

    # The QWidget widget is the base class of all user interface objectsdin 
    # PyQt5.
    # This provides a default constructor for QWidget (default has no parent).
    # A widget with no parent is called a window.
    window = QWidget()

    # The resize() method resizes the widget.
    # This one is 250px wide and 150px high.
    window.resize(250, 150)

    # The move() widget moves the widget to a position on screen.
    # Location is at coordinates 300x and 300y.
    window.move(300, 300)

    # This sets the titlebar title.
    window.setWindowTitle('Simple')

    # This displays the window on screen.
    window.show()

    # This enters the mainloop of the application, event handling starts from
    # this point. 
    # The mainloop receives the events from the window system and dispatches
    # them to the application widgets. 
    # The main loop ends if we call widget or if the main widget is destroyed.
    # The sys.exit call ensures a clean exit.
    # The only reason the exec_ was used with an underscore is because this
    # is a python keyword. 
    sys.exit(application_object.exec_())












