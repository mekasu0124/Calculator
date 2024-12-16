from src.utils.colors import ConsoleColors

from typing import Optional, Callable, Union, List

import time


class Printer:
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
        end: str = ""
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
                    print(f"{style}{char}{reset}", end=end, flush=True)
                    time.sleep(delay)
                print()
        else:
            for char in content:
                print(f"{style}{char}{reset}", end=end, flush=True)
                time.sleep(delay)
            print()

    @staticmethod
    def reset_console():
        """
        Resets the terminal completely, clearing all text and preventing scroll-back.
        """
        # ANSI sequence to clear the screen and disable scrollback buffer
        print("\033[3J\033[H\033[2J", end="")
    