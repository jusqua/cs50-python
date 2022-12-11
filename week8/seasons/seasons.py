from datetime import date
import re
import sys
import inflect


inflection = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    matches = re.fullmatch(r"(?:19[7-9]\d|2\d\d\d)-(?:1[0-2]|0[1-9])-(?:3[0-1]|[1-2]\d|0[1-9])", birth_date)
    if not matches:
        sys.exit("Invalid Date")

    try:
        birth_date = date.fromisoformat(matches.string)
    except ValueError:
        sys.exit("Invalid Date")

    print(convert(birth_date, date.today()))


def convert(birth_date: date, today_date: date) -> str:
    delta = today_date - birth_date
    minutes = round(delta.total_seconds() / 60)
    text = inflection.number_to_words(minutes, andword="").capitalize()

    return f"{text} minutes"


if __name__ == "__main__":
    main()
