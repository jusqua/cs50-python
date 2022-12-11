import re


def main():
    print(count(input("Text: ")))


def count(text: str) -> int:
    return len(re.findall(r"\bum\b", text, re.IGNORECASE))


if __name__ == "__main__":
    main()
