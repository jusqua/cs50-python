def main():
    fraction = get_fraction()

    if fraction >= 0.99:
        print("F")
    elif fraction <= 0.1:
        print("E")
    else:
        print(f"{round(fraction * 100)}%")


def get_fraction() -> float:
    while True:
        fraction = input('Fraction: ').strip()
        try:
            x, y = map(int, fraction.split("/"))
            if x > y or y == 0:
                continue
            return x / y
        except ValueError:
            pass


if __name__ == "__main__":
    main()
