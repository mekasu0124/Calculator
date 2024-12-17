# Python CLI Application with Docker

This is a simple Python CLI application built with Click and Docker.

## Features

1. `hello` command: Greets the user.
2. `calculate` command: Adds two numbers.

## Requirements

- Python 3.11+
- Docker

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/python-cli-docker-project.git
   cd python-cli-docker-project

## Usage

- General Commands:
  - Hello Command:
    - <code>docker run calculator:latest hello --name MyName</code>
      - returns <code>Hello, MyName!</code> to the console

  - Standard Calculator Commands
    - Addition
      - <code>docker run calculator:latest standard 1 + 2</code>
        - <code>>>> The sum of 1 and 2 is 3</code>
    - Subtraction
      - <code>docker run calculator:latest standard 1 - 2</code>
        - <code>>>> The difference of 1 and 2 is -1</code>
    - Multiplication
      - <code>docker run calculator:latest standard 1 x 2</code>
        - > NOTE: for multiplication, replace the asterisks * with an x otherwise the program will error. [See Other Notes](#other-notes)
        - <code>>>> The product of 1 and 2 is 2</code>
    - Division
      - <code>docker run calculator:latest standard 1 / 2</code>
        - <code>>>> The quotient of 1 and 2 is 0.5</code>
    - Raise a Number to the N-th Power
      - <code>docker run calculator:latest standard 1 ^ 2</code>
        - > NOTE: for squaring a number, replace the double asterisks ** with an up arrow ^ otherwise the program will error. [See Other Notes](#other-notes)
        - > NOTE: There are no separate functions for squaring, cubing, or n-power-ing a number. This function does it all.
        - <code>>>> The square of 1 and 2 is 1</code>
    - N-Root a Number (square-root, cube-root, n-root)
      - <code>docker run calculator:latest standard 1 ^^ 2</code>
        - <code>>>> The square-root of 1 is 1.0</code> where the <code>square-root</code> denotes the 2 input from the user
    - Multiply a Number by a Percentage
      - <code>docker run calculator:latest standard 50 % 20</code>
        - <code>50 * 20% is 10.0</code>
  - Scientific Calculator Commands
    - Log Base 2 (log2(n))
      - <code>docker run calculator:latest scientific 5 log2 0</code>
        - <code>>>> The log2(5) is 2.321928094887362</code>
      - <code>docker run calculator:latest scientific 5 log2 2</code>
        - <code>>>> The log2(5) is 2.321928094887362</code>
        - <code>>>> Rounded to 2 decimal places: 2.32</code>
      - <code>docker run calculator:latest scientific 5 log2 5</code>
        - <code>>>> The log2(5) is 2.321928094887362</code>
        - <code>>>> Rounded to 5 decimal places: 2.32193</code>

## Other Notes

When running the command, for example

<code>
sudo docker run calculator:latest calculate 3 * 5
</code>

the <code>*</code> causes the program to error with

<>
Usage: python -m cli_app.main calculate [OPTIONS] A OPERATION B
Try 'python -m cli_app.main calculate --help' for help.

Error: Invalid value for 'B': 'dockerfile' is not a valid integer.
</code>

Until I can figure out a solution to this problem, the correct way to use the command is to replace the <code>*</code> with an X <code>x</code> so the command will look like

- Linux:
  - <code>sudo docker run calculator:latest calculate 3 x 5</code>
