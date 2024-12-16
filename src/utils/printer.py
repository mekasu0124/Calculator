from enum import Enum
from typing import Optional, Callable, TypeVar, Union, List
import time


class ConsoleColors(Enum):
    # foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"

    # background colors
    BLACKB  = "\033[40m"
    REDB    = "\033[41m"
    GREENB  = "\033[42m"
    YELLOWB = "\033[43m"
    BLUEB   = "\033[44m"
    PURPLEB = "\033[45m"
    CYANB   = "\033[46m"
    WHITEB  = "\033[47m"

    # bold
    B    = "\033[1m"
    BOFF = "\033[22m"

    # italics
    I = "\033[3m"
    IOFF = "\033[23m"

    # underline
    U = "\033[4m"
    UOFF = "\033[24m"

    # invert
    R = "\033[7m"
    ROFF = "\033[27m"

T = TypeVar("T")


class Printer:
    @staticmethod
    def write(
        content: Union[str, List[str]], 
        color: ConsoleColors, 
        background: Optional[ConsoleColors] = None,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        invert: bool = False,
        end: str = "\n"
    ) -> None:
        
        style = color.value

        if background:
            style += background.value

        if bold:
            style += ConsoleColors.B.value

        if italic:
            style += ConsoleColors.I.value

        if underline:
            style += ConsoleColors.U.value

        if invert:
            style += ConsoleColors.R.value

        reset = ConsoleColors.RESET.value

        if isinstance(content, list):
            for line in content:
                print(f"{style}{line}{reset}", end=end)
        else:
            print(f"{style}{content}{reset}", end=end)

    """
    TODO: Update Function Below To Incorporate The Following:

    ? - break off error handling in else clause to use a different write function that uses a default red background, black text.
    """

    def get_string_from_console(
        self,
        prompt: str,
        color: ConsoleColors,
        background: Optional[ConsoleColors] = None,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        invert: bool = False,
        validator: Optional[Callable[[str], bool]] = None,
        error_message: Optional[str] = None,
        error_color: ConsoleColors = ConsoleColors.RED,
        use_typewriter: bool = False,
    ) -> str:
        """Get validated input from the user with styles."""
        while True:
            if use_typewriter:
                self.typewriter(
                    prompt,
                    color=color,
                    background=background,
                    bold=bold,
                    italic=italic,
                    invert=invert,
                    end="",
                )
            else:
                self.write(
                    prompt,
                    color=color,
                    background=background,
                    bold=bold,
                    italic=italic,
                    underline=underline,
                    invert=invert,
                    end="",
                )
            
            user_input = input()
            
            if validator is None or validator(user_input):
                return user_input
            
            if use_typewriter:
                self.typewriter(error_message or "Invalid Input.", error_color) 
            else:
                self.write(error_message or "Invalid input.", error_color)

    def get_from_console(
        self,
        prompt: str,
        color: ConsoleColors,
        parser: Callable[[str], T],
        validator: Optional[Callable[[T], bool]] = None,
        error_message: Optional[str] = None,
        error_color: ConsoleColors = ConsoleColors.RED,
        background: Optional[ConsoleColors] = None,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        invert: bool = False,
        use_typewriter: bool = False,
    ) -> T:
        
        while True:
            if use_typewriter:
                self.typewriter(
                    prompt,
                    color=color,
                    background=background,
                    bold=bold,
                    italic=italic,
                    invert=invert,
                )
            else:
                self.write(
                    prompt,
                    color=color,
                    background=background,
                    bold=bold,
                    italic=italic,
                    underline=underline,
                    invert=invert,
                    end=""
                )
                
            try:
                value = parser(input())
                
                if validator is None or validator(value):
                    return value
            except ValueError:
                pass
            
            
            if use_typewriter:
                self.typewriter(error_message or "Invalid Input.", error_color) 
            else:
                self.write(error_message or "Invalid input.", error_color)


    def typewriter(
        self,
        content: Union[str, List[str]],
        color: ConsoleColors,
        background: Optional[ConsoleColors] = None,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        invert: bool = False,
        delay: float = 0.04,
    ) -> None:
        
        style = color.value
        
        if background:
            style += background.value
        if bold:
            style += ConsoleColors.B.value
        if italic:
            style += ConsoleColors.I.value
        if underline:
            style += ConsoleColors.U.value
        if invert:
            style += ConsoleColors.R.value

        reset = ConsoleColors.RESET.value
        
        if isinstance(content, list):
            for line in content:
                for char in line:
                    print(f"{style}{char}{reset}", end="", flush=True)
                    time.sleep(delay)
                print()
        else:
            for char in content:
                print(f"{style}{char}{reset}", end="", flush=True)
                time.sleep(delay)
            print()

    @staticmethod
    def reset_console():
        """
        Resets the terminal completely, clearing all text and preventing scroll-back.
        """
        # ANSI sequence to clear the screen and disable scrollback buffer
        print("\033[3J\033[H\033[2J", end="")
    