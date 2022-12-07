from emoji import emojize


def main():
    code = input("Input: ")
    print("Output:", emojize(code, language="alias"))


if __name__ == "__main__":
    main()

