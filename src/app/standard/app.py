from typing import Callable

import math


class StandardCalculator:
    def __init__(self, printer, colors, helpers, json_engine):
        self.printer = printer
        self.colors = colors
        self.helpers = helpers
        self.json_engine = json_engine

        self.stop_callback = None

    def set_stop_callback(self, callback: Callable):
        self.stop_callback = callback

    def start(self):
        self.printer.reset_console()

        self.helpers.display_greeting()

        num1 = self.printer.get_from_console(
            prompt = "\nEnter First Number: ",
            color = self.colors.WHITE,
            parser = float,
            validator = lambda x: float(x),
            error_message = "Invalid Input. Input Must Be A Whole Number or Decimal. Try Again!",
            error_color = self.colors.RED
        )

        operation = self.printer.get_string_from_console(
            prompt = "\nSelect Operation (+, -, *, /, sqrt, percent): ",
            color = self.colors.WHITE,
            validator = lambda x: x in ["+", "-", "*", "/", "sqrt", "percent"],
            error_message = "Invalid Input. Input Must Be +, -, *, /, sqrt, percent. Try Again!",
            error_color = self.colors.RED
        )

        if operation not in ["sqrt", "percent"]:
            num2 = self.printer.get_from_console(
                prompt = "\nEnter Second Number: ",
                color = self.colors.WHITE,
                parser = float,
                validator = lambda x: float(x) or float(x) >= 0,
                error_message = "Invalid Input. Input Must Be A Whole Number or Decimal. Try Again!",
                error_color = self.colors.RED
            )

            valid_num1, valid_num2, valid_operation = self.validate_inputs(num1, num2, operation)

            solution = self.get_solution(valid_num1, valid_num2, valid_operation)
            print(solution)
        else:
            valid_num1, valid_operation = self.validate_inputs(num1, operation)

            solution = self.get_solution(valid_num1, valid_operation)
            print(solution)

            input("\nPress Enter To Continue...")

    def validate_inputs(self, num1: int, operation: str, num2: int = None) -> list:
        if num2:
            while operation == "/" and num2 == 0:
                self.printer.write("Cannot Divide By 0. Try Again", self.colors.RED)
                num2 = self.printer.get_from_console(
                    prompt = "Enter Second Number: ",
                    color = self.colors.WHITE,
                    parser = float,
                    validator = lambda x: float(x),
                    error_message = "Invalid Input. Cannot Divide By 0. Try Again!",
                    error_color = self.colors.RED
                )

                if operation == "/" and num2 > 0:
                    return [num1, num2, operation]
            
            return [num1, num2, operation]
        else:
            return [num1, operation]

    def get_solution(self, x: float, opera: str, y: float = None) -> str:
        if opera == "+":
            sum = x + y
        elif opera == "-":
            sum = x - y
        elif opera == "*":
            sum = x * y
        elif opera == "/":
            sum = x / y
        elif opera == "sqrt":
            sum = math.sqrt(x)
        elif opera == "percent":
            if x.is_integer():
                sum = x / 100
            else:
                return round(x*100)
            
        if y:
            new_solution = {
                "num1": x,
                "operation": opera,
                "num2": y,
                "solution": sum
            }

            txt = f"\n{x} {opera} {y} = {sum}"
        else:
            new_solution = {
                "num1": x,
                "operation": opera,
                "solution": sum
            }
            
            txt = f"\n{x} {opera} = {sum}"

        self.json_engine.save_to_history(new_solution)

        return txt
