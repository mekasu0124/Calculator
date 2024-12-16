class Helpers:
    def __init__(self):
        pass

    def display_greeting(self, printer, colors):
        text = [
            "~"*50,
            "\tWelcome To Calculator - Version 0.1.0",
            "~"*50
        ]

        return printer.typewriter(
            content = text,
            color = colors.BLUE,
            italic = True,
        )

    def display_contact(self, printer, colors):
        printer.reset_console()

        text = [
            "~"*50,
            "Welcome To Calculator - Version 0.1.0",
            "Author: mekasu0124",
            "GitHub: https://github.com/mekasu0124/Calculator",
            "Contact:",
            "\temail: mekasurenae@gmail.com",
            "\temail subject: RE: Calculator // <insert email title>",
            "~"*50
        ]

        return printer.typewriter(
            content = text,
            color = colors.CYAN,
            italic = True,
        )
