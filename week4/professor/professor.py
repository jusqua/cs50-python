from random import randint


def main():
    level = get_level()

    score = 0
    for _ in range(10):
        errors = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            if errors > 2:
                print(f"{x} + {y} = {x + y}")
                break
            try:
                answer = int(input(f"{x} + {y} = ").strip())
                if answer != x + y:
                    raise ValueError
            except ValueError:
                errors += 1
                print("EEE")
            else:
                score += 1
                break
    print("Score:", score)


def get_level() -> int:
    while True:
        level = input("Level: ").strip()
        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level: int) -> int:
    low = 10 ** (level - 1) - (not (level - 1))
    high = int("9" * level)
    return randint(low, high)


if __name__ == "__main__":
    main()

