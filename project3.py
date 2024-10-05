# project3.py
#
# ICS 33 Spring 2024
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.

from grin.interpreter import Interpreter


def get_lines():
    lines = []
    while True:
        line = input()
        if line.strip() == '.':
            break
        lines.append(line)
    return lines


def main() -> None:
    lines = get_lines()
    interpreter = Interpreter()
    interpreter.execute_program(lines)


if __name__ == '__main__':
    main()
