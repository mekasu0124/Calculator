from src.engines.db_engine import DbEngine
from src.engines.json_engine import JsonEngine
from src.utils.helpers import Helpers
from src.utils.printer import Printer, ConsoleColors

from src.app import Calculator


class Main:
    def __init__(self, db, json, helpers, printer, console_colors):
        self.db = db
        self.json = json
        self.helpers = helpers
        self.printer = printer
        self.colors = console_colors
        self.start()

    def start(self):
        self.helpers.display_greeting(self.printer, self.colors)

if __name__ == '__main__':
    running = True
    
    db_engine = DbEngine()
    json_engine = JsonEngine()
    helpers = Helpers()
    printer = Printer()
    console_colors = ConsoleColors()

    while running:
        Calculator(running, db_engine, json_engine, helpers, printer, console_colors)
