import gi, re

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

class NumberButtons(Gtk.Button):
        def __init__(self, label):
                Gtk.Button.__init__(self)
                self.set_label(label)
                self.set_size_request(80, 70)

class OperationButtons(Gtk.Button):
        def __init__(self, label):
                Gtk.Button.__init__(self)
                self.set_label(label)
                self.set_size_request()

class MainActivity(Gtk.Window):
    def __init__(self):

        self.screen = Gdk.Screen.get_default()
        self.provider = Gtk.CssProvider()
        self.style_context = Gtk.StyleContext()
        self.style_context.add_provider_for_screen(
            self.screen, self.provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        self.css = b"""
        window {
            background: white;
            font-size: 1.2rem;
            font-family: Roboto;
        }
        .result_label {
            background: #F0F0F0;
            color: black;
            border-radius: 6px;
            font-size: 1.5rem;
            font-weight: 700;
        }
        .delete_button {
            background: #EF5350;
            color: white;
        }
        button {
            background: #E0E0E0;
            color: black;
            border-radius: 6px;
            border-width: 1px;
            border-color: white;
        }
        button:hover {
            background: #BDBDBD;
        }
        button:active {
            background: #212121;
            color: white;
        }
        .button_op {
            background: #00E676;
        }
        """
        self.provider.load_from_data(self.css)

        self.expr = ""

        Gtk.Window.__init__(self, title="Calculator")
        window_context = self.get_style_context()
        window_context.add_class("window")

        self.set_resizable(False)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.result_label = Gtk.Label(label="ANS")

        label_context = self.result_label.get_style_context()
        label_context.add_class("result_label")

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
        self.button_decimal.connect("clicked", self.on_dec_button_clicked)

        self.button_calc = NumberButtons(label="=")
        self.button_calc.connect("clicked", self.on_eval_clicked)

        self.button_delete = NumberButtons(label="DEL")
        self.button_delete.connect("clicked", self.on_del_button_clicked)
        delete_context = self.button_delete.get_style_context()
        delete_context.add_class("delete_button")


        self.button_div = NumberButtons(label="/")
        self.button_div.connect("clicked", self.on_op_button_clicked)
        button_op_context = self.button_div.get_style_context()
        button_op_context.add_class("button_op")

        self.button_mul = NumberButtons(label="*")
        self.button_mul.connect("clicked", self.on_op_button_clicked)
        button_op_context = self.button_mul.get_style_context()
        button_op_context.add_class("button_op")

        self.button_sub = NumberButtons(label="-")
        self.button_sub.connect("clicked", self.on_op_button_clicked)
        button_op_context = self.button_sub.get_style_context()
        button_op_context.add_class("button_op")

        self.button_add = NumberButtons(label="+")
        self.button_add.connect("clicked", self.on_op_button_clicked)
        button_op_context = self.button_add.get_style_context()
        button_op_context.add_class("button_op")

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
        self.expr += button.get_label()
        self.result_label.set_label(self.expr)

    def on_op_button_clicked(self, button):
        oplist = ["+", "-", "*", "/"]
        op = button.get_label()
        try: 
            if self.result_label.get_label() != "ANS":
                if self.expr[-1] is not op and self.expr[-1] in oplist:
                    self.expr = self.expr[:-1] + op
                elif self.expr[-1] not in op:
                    self.expr += op
                self.result_label.set_label(self.expr)
        except IndexError:
            pass
    
    def on_dec_button_clicked(self, button):
        if self.result_label.get_label() != "ANS" and self.validate_expr(self.expr + "."):
            self.expr += button.get_label()
            self.result_label.set_label(self.expr)
        
    def on_eval_clicked(self, button): 
        try:
            self.expr = str(round(eval(self.expr), 6))
        except SyntaxError:
            pass
        self.result_label.set_label(str(self.expr))

    def on_del_button_clicked(self, button):
        if self.result_label.get_label() != "ANS" and self.expr != "":
            self.expr = self.expr[:-1]
            if self.expr == "":
                self.result_label.set_label("ANS")
            else:
                self.result_label.set_label(self.expr)

    def validate_expr(self, expression):
        regexp = r" *\d*\.?\d* *([\/\*\-\+] *\d*\.?\d* *)*"
        return bool(re.fullmatch(regexp, expression))

win = MainActivity()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
