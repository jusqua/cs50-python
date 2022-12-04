fruits = {
    'apple': 130,
    'banana': 110,
    'pear': 100,
    'sweet cherries': 100,
    'grapes': 90,
    'kiwifruit': 90,
    'orange': 80,
    'watermelon': 80,
    'plums': 70,
    'peach': 60,
    'nectarine': 60,
    'grapefruit': 60,
    'avocado': 50,
    'pineapple': 50,
    'tangerine': 50,
    'cantaloupe': 50,
    'strawberries': 50,
    'honeydew melon': 50,
    'lime': 20,
    'lemon': 15
}


def main():
    item = input('Item: ').strip().lower()
    if item in fruits:
        print('Calories:', fruits[item])


if __name__ == '__main__':
    main()

