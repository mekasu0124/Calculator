from src.utils.helpers import Helpers
from src.utils.printer import Printer, ConsoleColors


class Main:
    def __init__(self, running, helpers, printer, console_colors):
        self.running = running
        self.helpers = helpers
        self.printer = printer
        self.colors = console_colors

    def start(self):
        self.helpers.display_greeting(self.printer, self.colors)

        self.running = False
        return self.running

if __name__ == '__main__':
    running = True

    helpers = Helpers()
    printer = Printer()
    console_colors = ConsoleColors

    main = Main(running, helpers, printer, console_colors)

    while running:
        """
        * set the start function equal to the running variable so that
        * at any point throughout the program we call running = False
        * return running, it will stop the program as shown below and
        * in line 16 of the Main class above

        ! if you remove the variable re-declaration, you risk breaking the entire
        ! program. If you choose to replace this with another method, do so at
        ! your own risk.
        """
        running = main.start()
