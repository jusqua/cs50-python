import re


def main():
    print(convert(input("Hours: ")))


def convert(text: str) -> str:
    time = r"(?:(1[0-2]|(?<!\d)[1-9])(?::([0-5]\d))?) (?:(A|P)M)"
    matches = re.findall(time, text)
    formatting = re.search(f"{time} to {time}", text)

    if not formatting or len(matches) != 2:
        raise ValueError

    start, end = map(lambda t: f"{(int(t[0]) + (12 * (t[2] == 'P')) - (12 * (t[0] == '12'))):02}:{(int('0' + t[1])):02}", matches)
    return f"{start} to {end}"


if __name__ == "__main__":
    main()
