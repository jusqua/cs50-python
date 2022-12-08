import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        multiplier = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Request failed")
    else:
        data = response.json()
        rate = data["bpi"]["USD"]["rate_float"]
    currency = multiplier * rate
    print(f"${currency:,.4f}")


if __name__ == "__main__":
    main()

