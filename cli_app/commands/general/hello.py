import click


@click.command(name="hello")
@click.option("--name", default="World", help="Name to greet.")
def hello_command(name):
    """Gree the user."""
    click.echo(f"Hello, {name}!")
