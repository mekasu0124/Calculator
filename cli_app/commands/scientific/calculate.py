import click
import math


@click.command()
@click.argument("a", type=int)  # Pass the type object `int`
@click.argument("operation", type=str)
@click.argument("b", type=int)  # Pass the type object `int`
def scientific(a, operation, b = 0):
    """Return The Desired Sum Of Two Numbers"""

    if operation == "log10":
        result = math.log10(a)
    elif operation == "log2":
        result = math.log2(a)
    
    if b == 0:
        click.echo(f"The log2({a}) is {result}")
    else:
        click.echo(f"The log2({a}) is {result}")
        click.echo(f"Rounded to {b} decimal places: {round(result, b)}")
