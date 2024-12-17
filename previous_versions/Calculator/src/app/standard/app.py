from typing import Callable


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

        num2 = self.printer.get_from_console(
            prompt = "\nEnter Second Number: ",
            color = self.colors.WHITE,
            parser = float,
            validator = lambda x: float(x) or float(x) >= 0,
            error_message = "Invalid Input. Input Must Be A Whole Number or Decimal. Try Again!",
            error_color = self.colors.RED
        )

        operation = self.printer.get_string_from_console(
            prompt = "\nSelect Operation (+, -, *, /): ",
            color = self.colors.WHITE,
            validator = lambda x: x in ["+", "-", "*", "/"],
            error_message = "Invalid Input. Input Must Be +, -, *, or /. Try Again!",
            error_color = self.colors.RED
        )

        valid_num1, valid_num2, valid_operation = self.validate_inputs(num1, num2, operation)

        solution = self.get_solution(valid_num1, valid_num2, valid_operation)
        print(solution)

        input("\nPress Enter To Continue...")

    def validate_inputs(self, num1, num2, operation) -> list:
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

    def get_solution(self, x, y, opera) -> str:
        if opera == "+":
            sum = x + y
        elif opera == "-":
            sum = x - y
        elif opera == "*":
            sum = x * y
        elif opera == "/":
            sum = x / y

        new_solution = {
            "num1": x,
            "operation": opera,
            "num2": y,
            "solution": sum
        }

        self.json_engine.save_to_history(new_solution)

        return f"\n{x} {opera} {y} = {sum}"
