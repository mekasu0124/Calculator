from typing import Callable

import time
import math


class ScientificCalculator:
    def __init__(self, helpers):
        self.running = True
        self.stop_main_callback = None
        self.helpers = helpers

    def set_main_stop_callback(self, callback: Callable):
        """
        This function allows the Calculator class to be able to
        call the stop function within the root/main.py file to
        fully exit the program given user input option.
        """
        self.stop_main_callback = callback

    def start(self):
        while self.running:
            self.stop_main()

    def get_solution(self):
        pass

    def stop(self):
        self.running = False

    def stop_main(self):
        if self.stop_main_callback:
            self.stop_main_callback()