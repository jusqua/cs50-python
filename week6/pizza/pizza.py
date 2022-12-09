import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        sys.exit("Usage: python pizza.py [csv file]")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

