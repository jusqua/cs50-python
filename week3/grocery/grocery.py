def main():
    grocery = {}

    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    for key in sorted(grocery):
        print(grocery[key], key)


if __name__ == "__main__":
    main()
