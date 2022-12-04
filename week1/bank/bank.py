# Get greetings
greetings = input('Greeting: ').strip().lower()

# Check greetings
if (greetings.startswith('hello')):
    print('$0')
elif (greetings.startswith('h')):
    print('$20')
else:
    print('$100')
