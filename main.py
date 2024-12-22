from src.setup.config import Config

from src.utils.helpers import Helpers
from src.utils.menus import Menus

from src.app.main import StandardCalculator

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
            menu_options: Menus
        ):

        self.running = True

        self.config = config
        self.helpers = helpers
        self.menu_options = menu_options

    def start(self):
        # set the config to run outside the main loop
        # to ensure it only runs once per launch.
        self.config.start_setup()

        while self.running:
            self.helpers.print_title_bar()

            print("\n\nWhich Calculator Would You Like?\n")

            self.helpers.print_menu(self.menu_options.main)

            menu_choice = input("\nYour Selection (1-9): ")

            try:
                if int(menu_choice) == 1:
                    self.helpers.clear_console()

                    """
                    If you instantiate the StandardCalculator()
                    class down in the dunder name at the bottom
                    of the file, and pass it in through the Main()
                    class, it will not loop correctly when the user
                    elects to go back to the main menu from the 
                    standard calculator's menu options and then
                    attempts to go back into the StandardCalculator()
                    class.
                    """

                    calc = StandardCalculator(helpers, menu_options)
                    calc.set_main_stop_callback(main.stop)
                    calc.start()
                
                elif int(menu_choice) == 2:
                    self.helpers.clear_console()
                    print("Starting Scientific Calculator")
                
                elif int(menu_choice) == 8:
                    self.helpers.clear_console()
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
                self.helpers.clear_console()


    def stop(self):
        self.running = False


if __name__ == '__main__':
    config = Config()
    menu_options = Menus()

    helpers = Helpers()

    main = Main(config, helpers, menu_options)

    main.start()
