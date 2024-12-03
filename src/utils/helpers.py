

class Helpers:
    def __init__(self):
        pass

    def display_greeting(self, printer, colors):
        text = [
            "Welcome To Calculator - Version 0.1.0",
            "\n",
            "Author: mekasu0124",
            "GitHub: https://github.com/mekasu0124/Calculator",
            "Contact:",
            "\temail: mekasurenae@gmail.com",
            "\temail subject: RE: Calculator // <insert email title>"
        ]

        return printer.write(text, colors.CYAN)

        

    def display_menu(self):
        pass

