import re


def main():
    print(parse(input("HTML: ")))


def parse(html: str) -> str | None:
    short_url = None
    if matches := re.search(r'src="((?:https?:\/\/)(?:www\.)?(?:youtube\.com\/embed\/.*))"', html):
        url = matches.group(1)
        short_url = url.replace("youtube.com/embed", "youtu.be").replace("www.", "").replace("http:", "https:")
    return short_url


if __name__ == "__main__":
    main()
