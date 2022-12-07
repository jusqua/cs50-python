months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        current_date = input("Date: ").strip().title()
        try:
            if ',' in current_date:
                month, day, year = current_date.split()
                if month not in months:
                    continue
                month = months.index(month) + 1
                day = int(day[:-1])
                year = int(year)
            else:
                month, day, year = map(int, current_date.split("/"))

            if month > 12 or month < 1 or day > 31 or day < 1:
                continue
        except ValueError:
            pass
        else:
            break

    print(f"{year:04}-{month:02}-{day:02}")


if __name__ == "__main__":
    main()
