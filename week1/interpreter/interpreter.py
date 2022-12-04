def main():
    expression = input('Expression: ').strip()
    print(round(interpreter(expression), 1))


def interpreter(expression: str) -> float:
    x, op, y = expression.split()
    x = float(x)
    y = float(y)

    match op:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
    return x


if __name__ == '__main__':
    main()

