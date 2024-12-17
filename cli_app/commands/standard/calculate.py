import click
import math


@click.command()
@click.argument("a", type=int)  # Pass the type object `int`
@click.argument("operation", type=str)
@click.argument("b", type=int)  # Pass the type object `int`
def standard(a, operation, b):
    """Return The Desired Sum Of Two Numbers"""

    # add
    if operation == "+":
        result = a + b
        click.echo(f"The sum of {a} and {b} is {result}.")
    # subtract
    elif operation == "-":
        result = a - b
        click.echo(f"The difference of {a} and {b} is {result}")
    # multiply
    elif operation == "x":
        result = a * b
        click.echo(f"The product of {a} and {b} is {result}")
    # division
    elif operation == "/":
        try:
            result = a / b
            click.echo(f"The quotient of {a} and {b} is {result}")
        except ZeroDivisionError:
            click.echo("Cannot Divide By Zero. Try Again!")
        except Exception as e:
            raise e
    # a^b where number to raise is a and raised by is b
    elif operation == "^":
        result = a ** b
        click.echo(f"The square of {a}^{b} is {result}")

    # n-root of a where n is b
    elif operation == "^^":
        if b == 2:
            txt = "square-root"
            result = math.sqrt(a)
        elif b == 3:
            txt = "cube-root"
            result = math.cbrt(a)
        elif b > 3:
            txt = f"{b}th-root"
            result = math.pow(a,b)

        click.echo(f"The {txt} of {a} is {result}")

    # convert to percent
    elif operation == "%":
        result = a * (b/100)
        txt = f"{a} * {b}%"

        click.echo(f"{txt} is {result}")
