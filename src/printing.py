import sys

from colored import fore, back, style

def print_matrix(matrix, foreground, background, styling, outfile=sys.stdout):
    color: str = f"{style(styling)}{fore(foreground)}{back(background)}"

    for row in matrix:
        # scale horizontally by repeating chars
        line = [l + l + l for l in row]

        line = "".join(line)

        outfile.writelines(f"{color}{line}\n{style('reset')}")

    if outfile is not sys.stdout:
        outfile.flush()
