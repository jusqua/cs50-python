def main():
    fraction = input('Fraction: ').strip()
    print(gauge(convert(fraction)))


def convert(fraction: str) -> int:
    x, y = map(int, fraction.split("/"))
    if x > y:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage: int) -> str:
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

