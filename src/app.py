

class Calculator:
    def __init__(self, app_running, db_engine, json_engine, helpers):
        self.app_running = app_running
        self.db_engine = db_engine
        self.json_engine = json_engine
        self.helpers = helpers
        self.start()

    def start(self):
        """
        print welcome screen
        print menu to user

        get user menu input

        start corresponding calculator engine
        """
