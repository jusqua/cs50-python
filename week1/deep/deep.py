# Get answer
answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

# Treat answer
answer = answer.strip().replace('-', ' ').lower()

match answer:
    case '42' | 'forty two':
        print('Yes')
    case _:
        print('No')
