# root/main.py
from src.utils.colors import ConsoleColors
from src.utils.helpers import Helpers
from src.utils.printer import Printer

from src.app.engines.json_engine import JsonEngine

from src.app.standard.app import StandardCalculator


class Main:
    def __init__(self, printer, colors, helpers, json_engine, standard_calc):
        self.running = True  # Initialize running state here
        self.printer = printer
        self.colors = colors
        self.helpers = helpers
        self.json_engine = json_engine

        self.standard_calc = standard_calc

    def start(self):
        while self.running:  # Main loop embedded directly in the start method
            self.printer.reset_console()

            self.helpers.display_greeting()
            self.helpers.display_start_menu()

            valid_menu_choice = self.printer.get_string_from_console(
                prompt="\n>>> Your Selection (1, 2, C, H, Q): ",
                color=self.colors.WHITE,
                validator=lambda x: x in ["1", "2", "C", "H", "Q", "c", "h", "q"],
                error_message="Invalid Input. Input Must Be 1, 2, C, H, or Q. Try Again",
                error_color=self.colors.RED
            )

            if valid_menu_choice == "1":
                self.standard_calc.start()  # Call the standard calculator logic

            elif valid_menu_choice == "2":
                print("Scientific Calculator Chosen")
                # Placeholder for scientific calculator logic

            elif valid_menu_choice.lower() == "h":
                self.json_engine.get_history()

            elif valid_menu_choice.lower() == "c":
                self.helpers.display_contact()

            elif valid_menu_choice.lower() == "q":
                self.printer.write(
                    "Exiting Calculator... Please Wait...",
                    color=self.colors.BLACK
                )
                self.stop()

    def stop(self):
        self.running = False  # Breaks the main loop


if __name__ == '__main__':
    printer = Printer()
    colors = ConsoleColors

    json_engine = JsonEngine()

    helpers = Helpers(printer, colors)
    standard_calc = StandardCalculator(printer, colors, helpers, json_engine)

    main = Main(printer, colors, helpers, json_engine, standard_calc)

    standard_calc.set_stop_callback(main.stop)

    # Start the main application
    main.start()
