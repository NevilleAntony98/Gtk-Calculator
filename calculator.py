import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class MainActivity(Gtk.Window):
        def __init__(self):
                Gtk.Window.__init__(self, title="Calculator")

win = MainActivity()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
