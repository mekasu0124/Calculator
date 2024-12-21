from typing import Callable


class Calculator:
    def __init__(self, helpers, menu_options):
        self.running = True
        self.stop_main_callback = None

        self.helpers = helpers
        self.menu_options = menu_options

    def set_main_stop_callback(self, callback: Callable):
        self.stop_main_callback = callback

    def start(self):
        self.helpers.print_title_bar("Standard")

        self.helpers.print_menu(self.menu_options.standard)

        while self.running:
            print("Main Calculator Running")
            return self.stop_main()
        
    def stop(self):
        self.running = False

    def stop_main(self):
        if self.stop_main_callback:
            self.stop_main_callback()