from cli_app.commands.hello import hello_command
from cli_app.commands.calculate import calculate_command

import click


@click.group()
def cli():
    """Simple Python CLI Application"""
    pass


cli.add_command(hello_command)
cli.add_command(calculate_command)


if __name__ == '__main__':
    cli()
