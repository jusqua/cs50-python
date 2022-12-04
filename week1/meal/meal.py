def main():
    time = input('What time is it? ').strip().lower()

    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print('breakfast time')
    elif 12 <= converted_time <= 13:
        print('lunch time')
    elif 18 <= converted_time <= 19:
        print('dinner time')


def convert(time):
    if time.endswith('m.'):
        time, period = time.split()
        hours, minutes = time.split(':')
        if period.startswith('p'):
            hours = str(float(hours) + 12)
    else:
        hours, minutes = time.split(':')

    return float(hours) + float(minutes) / 60


if __name__ == '__main__':
    main()
