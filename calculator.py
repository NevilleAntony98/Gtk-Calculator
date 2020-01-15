import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class NumberButtons(Gtk.Button):
        def __init__(self, label):
                Gtk.Button.__init__(self)
                self.set_label(label)
                self.set_size_request(75, 50)

class OperationButtons(Gtk.Button):
        def __init__(self, label):
                Gtk.Button.__init__(self)
                self.set_label(label)
                self.set_size_request()

class MainActivity(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculator")

        grid = Gtk.Grid()
        self.add(grid)

        result_label = Gtk.Label(label="ANSWER")

        button0 = NumberButtons(label="0")
        button1 = NumberButtons(label="1")
        button2 = NumberButtons(label="2")
        button3 = NumberButtons(label="3")
        button4 = NumberButtons(label="4")
        button5 = NumberButtons(label="5")
        button6 = NumberButtons(label="6")
        button7 = NumberButtons(label="7")
        button8 = NumberButtons(label="8")
        button9 = NumberButtons(label="9")
        
        button_decimal = NumberButtons(label=".")
        button_calc = NumberButtons(label="=")

        button_delete = NumberButtons(label="DEL")
        button_div = NumberButtons(label="/")
        button_mul = NumberButtons(label="*")
        button_sub = NumberButtons(label="-")
        button_add = NumberButtons(label="+")

        grid.attach(result_label, 0, 0, 4, 1)
        grid.attach(button7, 0, 1, 1, 1)
        grid.attach_next_to(button8, button7, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button9, button8, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button4, button7, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5, button8, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button6, button9, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1, button4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2, button5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3, button6, Gtk.PositionType.BOTTOM, 1, 1)

        grid.attach_next_to(button_decimal, button1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button0, button2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button_calc, button3, Gtk.PositionType.BOTTOM, 1, 1)

        grid.attach_next_to(button_delete, result_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button_div, button_delete, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button_mul, button_div, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button_sub, button_mul, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button_add, button_sub, Gtk.PositionType.BOTTOM, 1, 1)


win = MainActivity()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
