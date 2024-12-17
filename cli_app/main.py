from cli_app.commands.general.hello import hello_command
from cli_app.commands.standard.calculate import standard
from cli_app.commands.scientific.calculate import scientific

import click


@click.group()
def cli():
    """
    A Simple Python CLI Calculator Application
    
    Use the commands below to interact with the application.
    """
    pass


cli.add_command(hello_command)
cli.add_command(standard)
cli.add_command(scientific)


if __name__ == '__main__':
    cli()
