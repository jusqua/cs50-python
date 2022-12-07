import sys
from pyfiglet import Figlet
from random import choice


def main():
    figlet = Figlet()

    if (len(sys.argv) not in [1, 3] or
        len(sys.argv) == 3 and sys.argv[1] not in ['-f', '--font']):
        sys.exit("Usage: python figlet.py [ -f | --font font_name]")

    if len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
    else:
        figlet.setFont(font=choice(figlet.getFonts()))

    text = input("Input: ").strip()
    print("Output:\n", figlet.renderText(text))


if __name__ == "__main__":
    main()

