import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    supported_formats = (".png", ".jpg", ".jpeg")
    if len(sys.argv) != 3 or not sys.argv[1].lower().endswith(supported_formats):
        sys.exit("Usage: python shirt.py [image input file] [image output file]")
    if splitext(sys.argv[1])[1].lower() != splitext(sys.argv[2])[1].lower():
        sys.exit("Error: I/O file extensions does not match")

    try:
        shirt = Image.open("shirt.png")
        image = ImageOps.fit(Image.open(sys.argv[1]), shirt.size)
        image.paste(shirt, mask=shirt)
        image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Error: \"{sys.argv[1]}\" does not exists")


if __name__ == "__main__":
    main()

