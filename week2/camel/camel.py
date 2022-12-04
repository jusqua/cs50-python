def main():
    camel_cased = input('camelCase: ').strip()
    print('snake_case:', camel_to_snake(camel_cased))


def camel_to_snake(camel_cased: str) -> str:
    snake_cased = ''
    for char in camel_cased:
        if (char.isupper()):
            snake_cased += '_' + char.lower()
        else:
            snake_cased += char
    return snake_cased


if __name__ == '__main__':
    main()
