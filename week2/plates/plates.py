def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(plate: str) -> bool:
    if len(plate) > 6 or len(plate) < 2:
        return False

    for char in plate[0:2]:
        if not char.isalpha():
            return False

    last_char = plate[1]
    is_any_number_found = False
    for char in plate[2:]:
        if (not char.isalnum() or 
           (last_char.isnumeric() and char.isalpha()) or
           (char.isnumeric() and char == '0' and not is_any_number_found)):
            return False

        if char.isnumeric():
            is_any_number_found = True
        last_char = char

    return True


if __name__ == '__main__':
    main()

