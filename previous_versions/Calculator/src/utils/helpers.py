class Helpers:
    def __init__(self, printer, colors):
        self.printer = printer
        self.colors = colors

    def display_greeting(self):
        text = [
            "~"*45,
            "    Welcome To Calculator - Version 0.1.0",
            "~"*45
        ]

        return self.printer.write(
            text,
            color = self.colors.BLUE
        )

    def display_contact(self):
        self.printer.reset_console()

        text = [
            "~"*75,
            "Welcome To Calculator - Version 0.1.0",
            "Author: mekasu0124",
            "GitHub: https://github.com/mekasu0124/Calculator",
            "Contact:",
            "\temail: mekasurenae@gmail.com",
            "\temail subject: RE: Calculator // <insert email title>",
            "Issues:",
            "\tgithub: https://github.com/mekasu0124/Calculator/issues",
            "Releases:",
            "\tgithub: https://github.com/mekasu0124/Calculator/releases/latest",
            "~"*75
        ]

        return self.printer.write(
            text,
            color = self.colors.CYAN,
        )
    
    def display_start_menu(self):        
        text = [
            "\n",
            "Which Calculator Would You Like?",
            "\n1. Standard",
            "2. Scientific",
            "H. View History",
            "C. Contact Us",
            "Q. Exit"
        ]

        self.printer.write(
            text,
            color = self.colors.PURPLE
        )
