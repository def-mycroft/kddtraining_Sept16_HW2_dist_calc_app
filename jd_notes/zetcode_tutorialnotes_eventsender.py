"""
http://zetcode.com/gui/pyqt5/eventssignals/
"""
# Events 
# All GUI applications are event-driven. 
# Events are generated mainly by the user of an application, but can be 
# by other means as well.
# When the exec_() method is called on the application, the application 
# enters the main loop. The main loop fetches events and sends them to objects.

# There are three participants in the event model:
# event source - the object whose state changes - generates events.
# event object - encapsulates the state changes into event source.
# event target - object that wants to be notified. 

# PyQt5 uses signals and slots to handle events - communication between
# objects. 
# a signal is emitted when an event occurs, a slot is any python callable.
