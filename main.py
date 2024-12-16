from src.utils.colors import ConsoleColors
from src.utils.helpers import Helpers
from src.utils.printer import Printer

from src.app.standard.app import StandardCalculator


class Main:
    def __init__(self, running, printer, colors, helpers, standard_calc):
        self.running = running
        self.printer = printer
        self.colors = colors
        self.helpers = helpers

        self.standard_calc = standard_calc

    def start(self):
        self.helpers.display_greeting()
        
        text = [
            "\n",
            "Which Calculator Would You Like?",
            "1. Standard",
            "2. Scientific",
            "C. Contact Us",
            "Q. Exit"
        ]

        self.printer.typewriter(
            content = text,
            color = self.colors.PURPLE,
            italic = True,
        )

        valid_menu_choice = self.helpers.get_user_input(
            "\n>>> Your Selection (1, 2, C, Q): ", 
            ["1", "2", "C", "Q", "c", "q"]
        )

        if valid_menu_choice == "1":
            self.standard_calc.start()
        
        elif valid_menu_choice == "2":
            print("Scientific Calculator Chosen")
            return self.stop()
        
        elif valid_menu_choice.lower() == "c":
            self.helpers.display_contact()
            self.start()

        elif valid_menu_choice.lower() == "q":
            self.printer.typewriter(
                content = "Exiting Calculator... Please Wait...",
                color = self.colors.BLACK,
                background = self.colors.YELLOWB,
                italic = True,
                bold = True,
                underline = True
            )

            return self.stop()

    def stop(self):
        self.running = False


if __name__ == '__main__':
    running = True

    printer = Printer()
    colors = ConsoleColors

    helpers = Helpers(printer, colors)

    standard_calc = StandardCalculator(printer, colors, helpers)

    main = Main(running, printer, colors, helpers, standard_calc)

    standard_calc.set_stop_callback(main.stop())

    while running:
        running = main.start()
