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
        self.result = ""

        Gtk.Window.__init__(self, title="Calculator")

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.result_label = Gtk.Label(label="0")

        self.button0 = NumberButtons(label="0")
        self.button0.connect("clicked", self.on_num_button_clicked)

        self.button1 = NumberButtons(label="1")
        self.button1.connect("clicked", self.on_num_button_clicked)

        self.button2 = NumberButtons(label="2")
        self.button2.connect("clicked", self.on_num_button_clicked)

        self.button3 = NumberButtons(label="3")
        self.button3.connect("clicked", self.on_num_button_clicked)

        self.button4 = NumberButtons(label="4")
        self.button4.connect("clicked", self.on_num_button_clicked)

        self.button5 = NumberButtons(label="5")
        self.button5.connect("clicked", self.on_num_button_clicked)

        self.button6 = NumberButtons(label="6")
        self.button6.connect("clicked", self.on_num_button_clicked)

        self.button7 = NumberButtons(label="7")
        self.button7.connect("clicked", self.on_num_button_clicked)

        self.button8 = NumberButtons(label="8")
        self.button8.connect("clicked", self.on_num_button_clicked)

        self.button9 = NumberButtons(label="9")
        self.button9.connect("clicked", self.on_num_button_clicked)
        
        self.button_decimal = NumberButtons(label=".")
        self.button_calc = NumberButtons(label="=")

        self.button_delete = NumberButtons(label="DEL")
        self.button_div = NumberButtons(label="/")
        self.button_mul = NumberButtons(label="*")
        self.button_sub = NumberButtons(label="-")
        self.button_add = NumberButtons(label="+")

        self.grid.attach(self.result_label, 0, 0, 4, 1)
        self.grid.attach(self.button7, 0, 1, 1, 1)
        self.grid.attach_next_to(self.button8, self.button7, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.button9, self.button8, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.button4, self.button7, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button5, self.button8, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button6, self.button9, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button1, self.button4, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button2, self.button5, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button3, self.button6, Gtk.PositionType.BOTTOM, 1, 1)

        self.grid.attach_next_to(self.button_decimal, self.button1, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button0, self.button2, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button_calc, self.button3, Gtk.PositionType.BOTTOM, 1, 1)

        self.grid.attach_next_to(self.button_delete, self.result_label, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.button_div, self.button_delete, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button_mul, self.button_div, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button_sub, self.button_mul, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button_add, self.button_sub, Gtk.PositionType.BOTTOM, 1, 1)
    
    def on_num_button_clicked(self, button):
        self.result += button.get_label()
        self.result_label.set_label(self.result)


win = MainActivity()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
