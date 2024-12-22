from typing import Callable

import time
import math


class StandardCalculator:
    def __init__(self, helpers, menu_options):
        self.running = True
        self.stop_main_callback = None # set the main applications stop function callback

        self.helpers = helpers
        self.menu_options = menu_options

    def set_main_stop_callback(self, callback: Callable):
        """
        This function allows the Calculator class to be able to
        call the stop function within the root/main.py file to
        fully exit the program given user input option.
        """
        self.stop_main_callback = callback

    def start(self):
        while self.running:
            self.helpers.print_title_bar("Standard")

            try:
                num1 = input("\nEnter First Number or 'Q' to quit: ")

                if num1.lower() == "q":
                    return self.stop()

                if "." in num1:
                    num1 = float(num1)
                else:
                    num1 = int(num1)

                operation = input("Enter Operation (+, -, *, /, sqrt, %): ")

                if operation not in ["sqrt", "%"]:
                    num2 = int(input("\nEnter Second Number: "))
                    result = self.get_solution(num1, operation, num2)
                else:
                    result = self.get_solution(num1, operation)

                print(result)
                self.wait_user_input()
            except Exception:
                valid_list = ["Whole Number", "Decimal Number", "+", "-", "*", "/", "sqrt", "%"]
                print(f"\nInvalid Input. Input Must Be: {', '.join(valid_list)}")
                self.wait_user_input()

    def get_solution(self, num1: float, operation: str, num2: float = None) -> str:
        if operation == "+":
            sum = num1 + num2
            return f"{num1} {operation} {num2} = {sum}"

        elif operation == "-":
            sum = num1 - num2
            return f"{num1} {operation} {num2} = {sum}"
        
        elif operation == "*":
            sum = num1 * num2
            return f"{num1} {operation} {num2} = {sum}"
        
        elif operation == "/":
            sum = num1 / num2
            return f"{num1} {operation} {num2} = {sum}"
        
        elif operation == "sqrt":
            sum = math.sqrt(num1)
            return f"√{num1} = {sum}"
        elif operation == "%":
            if num1 >= 1:
                sum = num1 / 100
                return f"The percent value of {num1} is {sum}%"
            else:
                sum = num1 * 100
                return f"The whole number value of {num1} is {sum}"

    def wait_user_input(self):
        input("Press Enter To Continue...")
        self.helpers.clear_console()
        
    def stop(self):
        """
        This stop() function is used to kick back out of
        the main calculators loop given user input option.

        self.stop => exit Calculator class
        self.stop_main_callback => exit program entirely
        """
        print("\nReturning To Main Menu...Please Wait...")
        time.sleep(2)
        self.running = False

    def stop_main(self):
        if self.stop_main_callback:
            self.stop_main_callback()