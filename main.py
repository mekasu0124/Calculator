from src.utils.helpers import Helpers
from src.utils.printer import Printer, ConsoleColors
from src.utils.menu_generator import MenuGenerator

from src.app.standard.app import StandardCalculator


class Main:
    """
    ? The Main class is what controls the applications
    ? life cycle, and which program runs based off user
    ? input.
    """
    def __init__(self, running, helpers, printer, console_colors, menu_gen, standard):
        """
        ? The main class is initialized with 4 properties:

        * - running => the boolean value that controls the life cycle of the application
        * - helpers => a utility class that has multi-use capabilities.
        * - printer, console_colors => from the printer utility class, allows colors to
        *   used in the console along with being able to have a typewriter effect for responses
        *   displayed to the user
        """
        
        self.running = running
        self.helpers = helpers
        self.printer = printer
        self.colors = console_colors
        self.menu_gen = menu_gen

        self.standard_calc = standard

    def start(self):
        """
        ? This method starts the program. It handles:

        * displaying the welcome messages to the user
        * obtaining user input from main menu on calculator selection or exiting program
        * calling the corresponding user desired calculator to run
        * ending the application life cycle upon user request
        """

        self.helpers.display_greeting(self.printer, self.colors)

        menu_choice = self.menu_gen.display_main_menu(self.printer, self.colors)

        if menu_choice == "1":
            self.standard_calc.start()

        elif menu_choice == "2":
            print("You Chose Scientific")

        elif menu_choice.lower() == "c":
            self.helpers.display_contact(self.printer, self.colors)
            self.start()

        elif menu_choice.lower() == "q":
            print("You Chose Exit")
            self.running = False
            return self.running
        else:
            print("Unknown Input")

if __name__ == '__main__':
    running = True

    helpers = Helpers()
    printer = Printer()
    console_colors = ConsoleColors
    menu_gen = MenuGenerator()

    standard = StandardCalculator(helpers, printer, console_colors, menu_gen)

    main = Main(running, helpers, printer, console_colors, menu_gen, standard)

    while running:
        """
        * set the start function equal to the running variable so that
        * at any point throughout the program we call running = False
        * return running, it will stop the program as shown below and
        * in line 16 of the Main class above

        ! if you remove the variable re-declaration, you risk breaking the entire
        ! program. If you choose to replace this with another method, do so at
        ! your own risk.
        """
        running = main.start()
