from enum import Enum
from typing import Optional, Callable, TypeVar, Union, List


class ConsoleColors(Enum):
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"


T = TypeVar('T')


class Printer:
    def write(self, object: Union[str, List[str]], color: ConsoleColors, end: str = '\n') -> None:
        if isinstance(object, list):
            for line in object:
                print(f"{color.value}{line}{ConsoleColors.RESET.value}", end=end)
        else:
            print(f"{color.value}{object}{ConsoleColors.RESET.value}", end=end)

    def write_ln(self, object: Union[str, List[str]], color: ConsoleColors):
        self.write(object, color, end='\n')

    def write_no_ln(self, object: Union[str, List[str]], color: ConsoleColors):
        self.write(object, color, end='')

    def get_string_from_console(
        self,
        prompt: str,
        color: ConsoleColors,
        validator: Optional[Callable[[str], bool]] = None,
        error_message: Optional[str] = None,
        error_color: ConsoleColors = ConsoleColors.RED
    ) -> str:
        while True:
            self.write_no_ln(prompt, color)
            input_str = input()
            if validator is None or validator(input_str):
                return input_str
            self.write_ln(error_message, error_color)

    # def get_from_console(
    #     self,
    #     prompt: str,
    #     color: ConsoleColors,
    #     parser: Callable[[str], T],
    #     validator: Optional[Callable[[T], bool]] = None,
    #     error_message: Optional[str] = None,
    #     error_color: ConsoleColors = ConsoleColors.RED
    # ) -> T:
    #     while True:
    #         self.write_no_ln(prompt, color)
    #         try:
    #             value = parser(input())
    #             if validator is None or validator(value):
    #                 return value
    #         except ValueError:
    #             pass
    #         self.write_ln(error_message, error_color)