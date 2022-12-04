def main():
    price = 50
    coins_allowed = [5, 10, 25]
    while price > 0:
        print('Amount Due:', price)
        coin = int(input('Insert Coin: ').strip())
        if coin in coins_allowed:
            price -= coin
    print('Change Owed:', -price)


if __name__ == '__main__':
    main()
