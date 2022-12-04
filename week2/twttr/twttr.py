def main():
    text = input('Input: ').strip()
    vowels = 'aeiou';

    for char in text:
        if (char.lower() in vowels):
            continue
        print(char, end='')
    print()


if __name__ == '__main__':
    main()

