import sys


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        sys.exit("Usage: python lines.py [python file]")

    counter = 0
    with open(sys.argv[1]) as file:
        for line in file:
            code_line = line.strip()
            if len(code_line) != 0 and not code_line.startswith("#"):
                counter += 1
    print(counter)


if __name__ == "__main__":
    main()

