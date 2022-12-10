import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    return bool(re.search(r"^(?:(?:1?\d{1,2}|2[0-4]\d|25[0-5])\.){3}(?:1?\d{1,2}|2[0-4]\d|25[0-5])$", ip))


if __name__ == "__main__":
    main()
