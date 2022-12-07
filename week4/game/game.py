from random import randint


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                continue
        except ValueError:
            pass
        else:
            break

    number = randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))
            if n < 1:
                continue
        except ValueError:
            continue
        if (guess > number):
            print("Too large!")
        elif (guess < number):
            print("Too small!")
        else:
            break

    print("Just right!")


if __name__ == "__main__":
    main()

