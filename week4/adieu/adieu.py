from inflect import engine


def main():
    plural = engine()

    names = []
    while True:
        try:
            names.append(input("Input: ").strip().title())
        except EOFError:
            break

    print("Adieu, adieu, to", plural.join(names))


if __name__ == "__main__":
    main()

