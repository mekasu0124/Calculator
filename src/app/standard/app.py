import math


class StandardCalculator:
    def __init__(self, helpers, printer, colors, menu_gen):
        self.helpers = helpers
        self.printer = printer
        self.colors = colors
        self.menu_gen = menu_gen

    def start(self):
        self.printer.reset_console()

        self.helpers.display_greeting(self.printer, self.colors)

        self.menu_gen.print_calculator_menu("standard", self.printer, self.colors)

        operator = self.printer.get_string_from_console(
            prompt = ">>> Your Selection (1-4): ",
            color = self.colors.WHITE,
            validator = lambda x: int(x) >= 1 and int(x) <= 4,
            error_message = "Invalid Input. Input Must Be A Whole Number 1-9",
            error_color = self.colors.RED
        )

        if operator == "1":
            print("Addition Selected")
        elif operator == "2":
            print("Subtraction Selected")
        elif operator == "3":
            print("Multiplication Selected")
        elif operator == "4":
            print("Division Selected")
