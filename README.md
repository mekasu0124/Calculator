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
