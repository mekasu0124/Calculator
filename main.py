from src.setup.config import Config

from src.utils.helpers import Helpers
from src.utils.menus import Menus

from src.app.main import Calculator

import time


class Main:
    """
    The Main() class handles the primary control
    and life cycle of the application itself. Each
    sub-calculator: Standard, Scientific, etc, are
    each setup on their own independent loop using
    a self.running = True instantiated within their
    dunder init method. Although there may be a better
    way to achieve the same goal, the goal itself is
    to allow the user to control when entering/exiting
    the sub-calculator based off their inputs within
    any part of the application.
    """

    def __init__(
            self, 
            config: Config, 
            helpers: Helpers, 
            menu_options: Menus,
            calc: Calculator
        ):

        self.running = True

        self.config = config
        self.helpers = helpers
        self.menu_options = menu_options

        self.calc = calc

    def start(self):
        # set the config to run outside the main loop
        # to ensure it only runs once per launch.
        self.config.start_setup()

        while self.running:
            self.helpers.print_title_bar()

            print("\n\nWhat Would You Like To Do?\n")

            self.helpers.print_menu(self.menu_options.main)

            menu_choice = input("\nYour Selection: ")

            try:
                if int(menu_choice) == 1:
                    print("\033[3J\033[H\033[2J")
                    self.calc.start()
                
                elif int(menu_choice) == 2:
                    print("\033[3J\033[H\033[2J")
                    print("Starting Scientific Calculator")
                
                elif int(menu_choice) == 8:
                    print("\033[3J\033[H\033[2J")
                    print("Loading User History")
                    print("")
                    history = self.helpers.get_user_history()
                    print(history)
                    print("")
                    input("Press Enter To Go Back...")

                elif int(menu_choice) == 9:
                    print("\nExiting The Program...Please Wait...")
                    time.sleep(0.5)
                    return self.stop()
                else:
                    print("\nInvalid Input. Input Must Be A Whole Number 1-9. Try Again")
            except Exception:
                print("\nInvalid Input. Input Must Be A Whole Number 1-9. Try Again!")
                print("If this problem persists, please contact support at mekshub@gmail.com")
                input("Press Enter To Continue...")
                print("\033[3J\033[H\033[2J")


    def stop(self):
        self.running = False


if __name__ == '__main__':
    config = Config()
    menu_options = Menus()

    helpers = Helpers()

    calc = Calculator(helpers, menu_options)
    main = Main(config, helpers, menu_options, calc)

    calc.set_main_stop_callback(main.stop)

    main.start()
