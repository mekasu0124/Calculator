from src.utils.triggers import Triggers

class MenuGenerator:
    def display_main_menu(self, printer, colors):
        text = [
            "Which Calculator Would You Like?",
            "\n",
            "1. Standard",
            "2. Scientific",
            "C. Contact",
            "Q. Exit"
        ]

        printer.typewriter(
            content = text,
            color = colors.PURPLE,
            italic = True,
        )

        return printer.get_string_from_console(
            prompt = "\n>>> Your Selection (1-9/C/Q): ",
            color = colors.WHITE,
            validator = lambda x: x in ["1","2","C","c","Q","q"],
            error_message = "\nInvalid Input. Input Must Be A Whole Number 1-9 or 'Q' for Quit",
            error_color = colors.RED
        )
    
    def print_calculator_menu(self, trigger, printer, colors):
        triggers = Triggers()

        standard_list = triggers.standard
        scientific_list = triggers.scientific

        printer.typewriter(
            content = "\nWhich Operation Would You Like?\n",
            color = colors.CYAN,
            italic = True
        )

        if trigger == "standard":
            printer.typewriter(
                content = standard_list,
                color = colors.PURPLE,
                italic = True
            )

        elif trigger == "scientific":
            printer.typewriter(
                content = scientific_list,
                color = colors.PURPLE,
                italic = True
            )
