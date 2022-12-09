import sys
import csv


def main():
    if len(sys.argv) != 3 or not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Usage: python scourgify.py [csv input file] [csv output file]")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            data = []
            for student in reader:
                last, first = student["name"].split(", ")
                data.append({ "first": first, "last": last, "house": student["house"]})
    except FileNotFoundError:
        sys.exit(f"Error: \"{sys.argv[1]}\" does not exists")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    main()

