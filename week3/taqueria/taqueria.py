entries = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    amount = 0.0
    while True:
        try:
            entry = input("Item: ").strip().title()
            if entry in entries:
                amount += entries[entry]
                print(f"${amount:.2f}")
        except EOFError:
            break


if __name__ == "__main__":
    main()
