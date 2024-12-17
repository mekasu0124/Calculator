import click


@click.command(name="calculate")
@click.argument("a", type=int)  # Pass the type object `int`
@click.argument("operation", type=str)
@click.argument("b", type=int)  # Pass the type object `int`
def calculate_command(a, operation, b):
    """Return The Desired Sum Of Two Numbers"""

    if operation == "+":
        result = a + b
        click.echo(f"The sum of {a} and {b} is {result}.")
    elif operation == "-":
        result = a - b
        click.echo(f"The difference of {a} and {b} is {result}")
    elif operation == "x":
        result = a * b
        click.echo(f"The product of {a} and {b} is {result}")
    elif operation == "/":
        try:
            result = a / b
            click.echo(f"The quotient of {a} and {b} is {result}")
        except ZeroDivisionError:
            click.echo("Cannot Divide By Zero. Try Again!")
        except Exception as e:
            raise e
