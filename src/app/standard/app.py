from typing import Callable


class StandardCalculator:
    def __init__(self, printer, colors, helpers):
        self.printer = printer
        self.colors = colors
        self.helpers = helpers

        self.stop_callback = None

    def set_stop_callback(self, callback: Callable):
        self.stop_callback = callback

    def start(self):
        self.printer.reset_console()

        self.helpers.display_greeting()
