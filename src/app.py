from src.utils.helpers import Helpers


class Calculator:
    def __init__(self, app_running):
        self.app_running = app_running

        self.helpers = Helpers()

        self.start()

    def start(self):
        """
        print welcome screen
        print menu to user

        get user menu input

        start corresponding calculator engine
        """
        user_menu_choice = self.helpers.display_menu()

