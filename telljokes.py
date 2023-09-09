import random

def read_jokes(filename):
    with open(filename, "r") as file:
        jokes = file.read().splitlines()
    return jokes

def tell_joke(jokes):
    random_joke = random.choice(jokes)
    print("Joke of the moment:")
    print(random_joke)
    print("-------------------------------")

# Example usage
jokes_filename = "jokes.txt"  # Replace with your jokes file name
jokes = read_jokes(jokes_filename)

# Main program loop
while True:
    tell_joke(jokes)
    input("Press Enter to tell another joke or Ctrl+C to exit...")
