def main():
    word = input('Input: ').strip()
    print(shorten(word))


def shorten(word: str) -> str:
    vowels = 'aeiou';
    short_word = ''
    for char in word:
        if (char.lower() in vowels):
            continue
        short_word += char
    return short_word


if __name__ == '__main__':
    main()

