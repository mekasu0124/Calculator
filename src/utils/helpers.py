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

        return self.printer.typewriter(
            content = text,
            color = self.colors.BLUE,
            italic = True,
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

        return self.printer.typewriter(
            content = text,
            color = self.colors.CYAN,
            italic = True,
        )
    
    def get_user_input(self, prompt: str, valid_inputs: list):
        choice = input(prompt)

        while not choice in valid_inputs:
            self.printer.typewriter(
                prompt = f"\nInvalid Input. Input Must Be: {', '.join(valid_inputs)}",
                color = self.colors.BLACK,
                background = self.colors.REDB,
                bold = True,
                italic = True,
                underline = True
            )

            choice = input(f"\n{prompt}")

            if self.validators.is_number(choice):
                return choice
        
        return choice
